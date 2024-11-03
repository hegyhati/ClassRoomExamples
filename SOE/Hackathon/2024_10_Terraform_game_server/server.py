from copy import deepcopy
from functools import partial
import random
from sys import argv
from threading import Thread
import threading
import time
from flask import Flask, request
from game import Game, GameParams
from enum import Enum
import os
import requests
from flask_cors import CORS
import conf
import json


class GameState(Enum):
    WAITING_FOR_PLAYERS = 0
    ACTIVE = 1
    FINISHED = 2


# cd to engine/
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# global variables
game_state: GameState = GameState.WAITING_FOR_PLAYERS
state_json_cache: dict = {}
level_path: str = argv[1] if len(argv) > 1 else conf.DEFAULT_LEVEL_PATH
assert level_path.endswith(".json")
with open(level_path, encoding="utf-8") as f:
    game_params: GameParams = json.load(f)
lobby: dict[str, str] = {}
secrets: dict[str, str] = {}
deploy_queue: list[tuple[str, int, int, int]] = []

lock = threading.Lock()

server = Flask(__name__)
CORS(server)


@server.get("/state")
def get_state():
    match game_state:
        case GameState.WAITING_FOR_PLAYERS:
            return {
                "state": "Waiting for teams...",
                "teams_in_lobby": lobby,
                "teams_remaining": game_params["team_count"] - len(lobby)
            }
        case GameState.FINISHED:
            return {
                "state": "Game has ended.",
                **state_json_cache
            }
        case GameState.ACTIVE:
            return {
                "state": "Game is active.",
                **state_json_cache
            }



def is_valid_ip(ip: str) -> bool:
    if ip == "host.docker.internal":
        return True
    if ip.count(".") != 3:
        return False
    try:
        nums = [int(num) for num in ip.split(".")]
    except ValueError:
        return False
    for num in nums:
        if num < 0 or num > 255:
            return False
    return True

@server.post("/register")
def register_team():
    global lobby
    global secrets

    if game_state != GameState.WAITING_FOR_PLAYERS:
        return {"error" : "Game already started."}

    team_name = request.args.get("name")
    ip = request.args.get("ip")
    if team_name is None:
        return {"error": "Team name not provided."}
    if ip is None:
        return {"error": "IP address is not provided."}
    if not is_valid_ip(ip):
        return {"error": f"Not a valid ip address: {ip}"}
    with lock:
        if team_name in lobby:
            return {"error": f"Team {team_name} already registered."}
        if len(lobby) == game_params["team_count"]:
            return {"error": "Game already has enough teams."}
        lobby[team_name] = ip
        secrets[team_name] = str(random.randrange(10**6))
        if len(lobby) == game_params["team_count"]:
            Thread(target=game_loop).start()
        return {
            "id": len(secrets) - 1,
            "secret": secrets[team_name]
        }


@server.post("/deploy")
def deploy_new_robot():
    global deploy_queue
    team_name = request.args.get("name")
    team_secret = request.args.get("team_secret")
    if team_name is None or team_name not in secrets or secrets[team_name] != team_secret:
        return {"error": "Authentication error."}
    try:
        robot_id = int(request.args["robot_id"])
        robot_row = int(request.args["robot_row"])
        robot_col = int(request.args["robot_col"])
    except (ValueError, TypeError, KeyError):
        return {"error": "Invalid robot ID or coordinates."}
    with lock:
        deploy_queue.append((team_name, robot_id, robot_row, robot_col))
    return {"success": f"Deploying robot {robot_id} for team {team_name} around position {robot_row, robot_col} in progress..."}


def get_next_action(ip: str, team: str, robot_id: int, result_dict: dict[str, dict[int, Game.Robot.Action]]) -> None:
    try:
        response = requests.get(
            f"http://{ip}:{conf.MANDATORY_PORT}/bot/{robot_id}",
            json={
                "gamestate": state_json_cache,
                "team": team
            },
            timeout=conf.ROBOT_REQUEST_TIMEOUT
        )
        if response.ok:
            result_dict[team][robot_id] = Game.Robot.Action(response.text)
    except (requests.ConnectTimeout, ValueError, TypeError,requests.exceptions.ConnectionError):
        return


def request_all_bot_actions() -> dict:
    actions = {team: {} for team in lobby}
    for team, robots in state_json_cache["robots"].items():
        for robot_id, robot in enumerate(robots):
            if robot is not None:
                Thread(target=partial(get_next_action, lobby[team], team, robot_id, actions)).start()
    time.sleep(conf.TURN_DURATION)
    return deepcopy(actions)  # just to be safe if thread takes longer than 1s


def parse_deployments():
    global deploy_queue
    with lock:
        current_deploy, deploy_queue = deploy_queue, []
    return {
        team_name: {
            robot_id: (row, col)
            for (team, robot_id, row, col) in current_deploy if team == team_name
        } for team_name in set(d[0] for d in current_deploy)
    }


def game_loop():
    global state_json_cache
    global game_state


    game: Game | None = Game(list(lobby), game_params)
    assert game is not None
    state_json_cache = game.get_state_json()
    game_state = GameState.ACTIVE

    for _ in range(game_params["round_count"]):
        if game_state != GameState.ACTIVE: 
            return
        game.make_turn(request_all_bot_actions(), parse_deployments())
        state_json_cache = game.get_state_json()
        print(state_json_cache)
        print(game)
    game_state = GameState.FINISHED


@server.post("/reset")
def reset_game():
    global game_state
    global game_params

    data = request.get_json()
    if "secret" not in data or data["secret"] != "mindmeghalunk":
        return "Not today"

    game_state = GameState.WAITING_FOR_PLAYERS
    time.sleep(conf.TURN_DURATION)
    state_json_cache.clear()
    lobby.clear()
    secrets.clear()
    deploy_queue.clear()


    level_path: str = data["level"] if "level" in data else conf.DEFAULT_LEVEL_PATH
    assert level_path.endswith(".json")
    with open(level_path, encoding="utf-8") as f:
        game_params = json.load(f)
        print(game_params)
    if "turn_duration" in data: 
        conf.TURN_DURATION = float(data["turn_duration"])
    if "robot_request_timeout" in data:
        conf.ROBOT_REQUEST_TIMEOUT = float(data["robot_request_timeout"])
    
    return get_state()




server.run(host="0.0.0.0", threaded=True, processes=1)
