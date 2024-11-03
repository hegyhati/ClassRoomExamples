from enum import Enum
import json
import random
from typing import Any, Optional,TypedDict


class GameParams(TypedDict):
    map_file: str
    round_count: int
    team_count: int
    max_robots: int
    max_paint_level: int
    boom_range: int
    boom_timeout: int
    min_paint_for_boom: int


class Game:

    class Block(Enum):
        WALL = -1
        CLEAR = 0
        PLAYER_1 = 1
        PLAYER_2 = 2
        PLAYER_3 = 3
        PLAYER_4 = 4
        PLAYER_5 = 5
        PLAYER_6 = 6
        PLAYER_7 = 7
        PLAYER_8 = 8

        @classmethod
        def _missing_(cls, value: object) -> Any:
            match(value):
                case "#": return cls.WALL
                case " ": return cls.CLEAR
                case str() as num if num in "123456789": return cls(int(num))
                case int() as num if num in list(range(1, cls.max_player() + 1)): return cls(num)
            return super()._missing_(value)

        def __str__(self) -> str:
            match(self):
                case Game.Block.WALL: return "█"
                case Game.Block.CLEAR: return "░"
                case _: return f"\033[{40 + self.value}m \033[0m"

        @staticmethod
        def max_player() -> int:
            return max(e.value for e in Game.Block)

    class Robot:

        class Action(Enum):
            UP = (-1, 0)
            DOWN = (1, 0)
            LEFT = (0, -1)
            RIGHT = (0, +1)
            BOOM = (0, 0)

            @classmethod
            def _missing_(cls, value: object) -> Any:
                str_to_action = {
                    "boom": Game.Robot.Action.BOOM,
                    "up": Game.Robot.Action.UP,
                    "down": Game.Robot.Action.DOWN,
                    "left": Game.Robot.Action.LEFT,
                    "right": Game.Robot.Action.RIGHT,
                }
                match(value):
                    case str() as action if action in str_to_action:
                        return cls(str_to_action[action])
                return super()._missing_(value)

        class State(Enum):
            ACTIVE = 1
            SELF_DESTRUCTION = 2
            DEAD = 0

        # constants set from GameParams
        INITIAL_PAINT_LEVEL: int
        BOOM_RANGE: int
        SELF_DESTRUCTION_TIMEOUT: int
        PAINT_LEVEL_FOR_SELF_DESTRUCTION: int

        __current_id = 0

        @classmethod
        def get_next_robot_id(cls):
            cls.__current_id += 1
            return cls.__current_id

        def __init__(self, team_id: int, pos_row: int, pos_col: int, game: "Game") -> None:
            if team_id < 1 or team_id > Game.Block.max_player():
                raise ValueError(f"Invalid player id: {team_id}")
            self._team: int = team_id
            self._row: int = pos_row
            self._col: int = pos_col
            self._paint: int = Game.Robot.INITIAL_PAINT_LEVEL
            self._state: "Game.Robot.State" = Game.Robot.State.ACTIVE
            self._game: "Game" = game
            self._uid = self.get_next_robot_id()

        def __str__(self) -> str:
            return f"\033[30;{40 + self._team}m{'⊡' if self.is_alive() else '⊠'}\033[0m"

        def is_alive(self) -> bool:
            return self._state != Game.Robot.State.DEAD

        def position(self) -> tuple[int, int]:
            return self._row, self._col

        def _boom(self) -> None:
            for r in range(-Game.Robot.BOOM_RANGE, Game.Robot.BOOM_RANGE + 1):
                for c in range(-Game.Robot.BOOM_RANGE, Game.Robot.BOOM_RANGE + 1):
                    if abs(r) + abs(c) <= Game.Robot.BOOM_RANGE:
                        try:
                            self._game.paint_block(self._row + r, self._col + c, self._team, check_robot=True)
                        except ValueError:
                            pass

            self._state = Game.Robot.State.DEAD

        def _shutdown(self) -> None:
            self._state = Game.Robot.State.DEAD

        def _move(self, action: "Game.Robot.Action") -> bool:
            new_row: int = self._row + action.value[0]
            new_col: int = self._col + action.value[1]
            if self._game.is_wall(new_row, new_col):
                return False
            self._row, self._col = new_row, new_col
            if self._game.get_block(self._row, self._col).value != self._team:
                self._game.paint_block(self._row, self._col, self._team)
                self._paint -= 1
                if self._paint == 0:
                    self._shutdown()
            return True

        def do(self, action: Optional["Game.Robot.Action"] = None) -> bool:
            if self.is_alive():
                match(self._state, action):
                    case Game.Robot.State.ACTIVE, None: return True
                    case Game.Robot.State.SELF_DESTRUCTION, None:
                        self._turns_until_boom -= 1
                        if self._turns_until_boom == 0:
                            self._boom()
                        return True
                    case Game.Robot.State.ACTIVE, Game.Robot.Action.BOOM:
                        if self._paint < Game.Robot.PAINT_LEVEL_FOR_SELF_DESTRUCTION:
                            return False
                        self._turns_until_boom: int = Game.Robot.SELF_DESTRUCTION_TIMEOUT
                        self._state = Game.Robot.State.SELF_DESTRUCTION
                        return True
                    case Game.Robot.State.ACTIVE, action if action is not None:
                        return self._move(action)
                    case _: return False
            return False

    def __init__(self, team_names: list[str], params: GameParams) -> None:
        if len(team_names) != len(set(team_names)):
            raise ValueError("Multiple teams with the same name.")
        if len(team_names) == 0:
            raise ValueError("At least one team is needed.")
        if len(team_names) > Game.Block.max_player():
            raise ValueError(f"At most {Game.Block.max_player()} teams can be added.")
        Game.Robot.INITIAL_PAINT_LEVEL = params["max_paint_level"]
        Game.Robot.BOOM_RANGE = params["boom_range"]
        Game.Robot.SELF_DESTRUCTION_TIMEOUT = params["boom_timeout"]
        Game.Robot.PAINT_LEVEL_FOR_SELF_DESTRUCTION = params["min_paint_for_boom"]

        self.__max_robots: int = params["max_robots"]
        self.__init_map_from_file(params["map_file"])
        self.__init_teams_and_robots(team_names)
        self.__round: int = 0
        self.__round_count: int = params["round_count"]
        self.__last_events: list[dict] = []

    def __init_map_from_file(self, filename: str) -> None:
        with open(filename) as f:
            self.__map: list[list["Game.Block"]] = [
                [Game.Block(c) for c in line.strip()]
                for line in f
            ]
        self.__rows: int = 2 + len(self.__map)
        self.__columns: int = 2 + max(len(line) for line in self.__map)
        self.__map.insert(0, [])
        self.__map.append([])
        for line in self.__map:
            line.insert(0, Game.Block.WALL)
            line.extend([Game.Block.WALL] * (self.__columns - len(line)))

    def __init_teams_and_robots(self, team_names: list[str]) -> None:
        self.__team_id: dict[str, int] = {
            name: idx + 1
            for idx, name in enumerate(team_names)
        }
        self.__scores: dict[str, int] = {
            name: 0
            for name in team_names
        }
        self.__robots: dict[str, list["Game.Robot | None"]] = {
            name: [None] * self.__max_robots
            for name in team_names
        }

    def __get_robots_at_position(self, row: int, col: int) -> list["Game.Robot"]:
        return [robot for team in self.__robots for robot in self.__robots[team] if robot is not None and robot.position() == (row, col)]

    def __str_pos__(self, row: int, col: int) -> str:
        match self.__get_robots_at_position(row, col):
            case []: return str(self.__map[row][col])
            case [robot]: return str(robot)
            case _: return "⊠"

    def __str__(self) -> str:
        return "\n".join([
            "".join(self.__str_pos__(row, col) for col, block in enumerate(line))
            for row, line in enumerate(self.__map)
        ])

    def __find_closest_free_position(self, team: str, row: int, col: int) -> tuple[int, int] | None:
        # TODO make splash radius parametrized
        CHECK_ORDER = [(0, 0), (0, 1), (1, 0), (-1, 0), (0, -1), (2, 0), (1, 1), (0, 2), (-1, 1), (-2, 0), (-1, -1), (0, -2), (1, -1)]

        for r, c in CHECK_ORDER:
            try:
                if self.get_block(row + r, col + c) == Game.Block(self.__team_id[team]) and self.__get_robots_at_position(row + r, col + c) == []:
                    return row + r, col + c
            except ValueError:
                pass
        return None

    def is_wall(self, row: int, col: int) -> bool:
        return self.get_block(row, col) == Game.Block.WALL

    def get_block(self, row: int, col: int) -> "Game.Block":
        if row < 0 or row >= self.__rows or col < 0 or col >= self.__columns:
            raise ValueError("Out of bound row/col.")
        return self.__map[row][col]

    def paint_block(self, row: int, col: int, team_id: int | None = None, check_robot: bool = False) -> None:
        if team_id is not None and (team_id < 1 or team_id) > Game.Block.max_player():
            raise ValueError(f"Incorrect team id: {team_id}")
        if row < 0 or row >= self.__rows or col < 0 or col >= self.__columns:
            raise ValueError("Incorrect row, col.")
        if not self.is_wall(row, col) and (not check_robot or self.__get_robots_at_position(row, col) == []):
            self.__map[row][col] = Game.Block.CLEAR if team_id is None else Game.Block(team_id)

    def add_robot(self, team: str, row: int, col: int, robot_id: int | None = None):
        if team not in self.__team_id:
            raise ValueError("Incorrect team name.")
        if robot_id is not None:
            if robot_id < 0 or robot_id >= self.__max_robots:
                raise ValueError(f"Incorrect robot id, should be between 0 and {self.__max_robots - 1}")
            if self.__robots[team][robot_id] is not None:
                raise ValueError(f"Robot for team {team} with id {robot_id} already in the game.")
        else:
            for id in range(self.__max_robots):
                if self.__robots[team][id] is None:
                    robot_id = id
                    break
            if robot_id is None:
                raise ValueError(f"Team {team} has all its robots in the game.")
        position: tuple[int, int] | None = self.__find_closest_free_position(team, row, col)
        if position is None:
            raise ValueError(f"Cannot place robot for team {team} near {row},{col}.")
        self.__robots[team][robot_id] = Game.Robot(self.__team_id[team], *position, game=self)

    def make_turn(self, actions: dict[str, dict[int, "Game.Robot.Action"]], deployments: dict[str, dict[int, tuple[int, int]]]) -> None:
        self.__last_events = []
        # Execute wait, if robot explodes, remove it.
        boom_robots = [(team, idx) for team, robots in self.__robots.items()
                       for idx, robot in enumerate(robots)
                       if robot is not None and robot._state == Game.Robot.State.SELF_DESTRUCTION]
        random.shuffle(boom_robots)
        for team, idx in boom_robots:
            robot = self.__robots[team][idx]
            if robot is None:
                continue
            robot.do()
            if not robot.is_alive():
                self.__robots[team][idx] = None
                self.__last_events.append((
                    {
                        "event": "explosion",
                        "team": team,
                        "robot_id": idx,
                        "row": robot._row,
                        "col": robot._col,
                        "robot_uid": robot._uid
                    }
                ))
        # Execute moving actions and starting of self destruction
        for team, robot_actions in actions.items():
            for robot_id, action in robot_actions.items():
                robot: "Game.Robot|None" = self.__robots[team][robot_id]
                if robot is not None and robot.do(action):
                    self.__last_events.append({
                        "event": action.name,
                        "team": team,
                        "robot_id": robot_id,
                        "row": robot._row,
                        "col": robot._col,
                        "robot_uid": robot._uid
                    })
        # Check collisions and remove dead robots (not efficient)
        for row in range(self.__rows):
            for col in range(self.__columns):
                robots = self.__get_robots_at_position(row, col)
                if len(robots) > 1:
                    if len({robot._team for robot in robots}) > 1:
                        self.paint_block(row, col)
                    for robot in robots:
                        robot._shutdown()
                    self.__last_events.append({
                        "event": "collision",
                        "row": row,
                        "col": col
                    })
        for team, robots in self.__robots.items():
            for idx, robot in enumerate(robots):
                if robot is not None and not robot.is_alive():
                    robots[idx] = None
        # Execute deployments
        for team, deployment in deployments.items():
            for robot_id, (row, col) in deployment.items():
                try:
                    self.add_robot(team, row, col, robot_id)  # Note: add_robot handles robot_id==None, but this function expects it.
                    self.__last_events.append({
                        "event": "deploy",
                        "team": team,
                        "robot_id": robot_id,
                        "row": self.__robots[team][robot_id]._row,  # type: ignore
                        "col": self.__robots[team][robot_id]._col,  # type: ignore
                        "robot_uid": self.__robots[team][robot_id]._uid  # type: ignore
                    })
                except ValueError as e:
                    print(f"Error at deploy step: {team} - {deployment} - {e}")
        # Update scores
        for team_name, team_id in self.__team_id.items():
            for row in range(self.__rows):
                for col in range(self.__columns):
                    if self.get_block(row, col).value == team_id:
                        self.__scores[team_name] += 1 + self.__round // 10
        self.__round += 1

    def get_state_json(self, indent: int | None = None) -> dict:
        return {
            "meta": {
                "round": self.__round,
                "round_count": self.__round_count,
                "max_paint_level": Game.Robot.INITIAL_PAINT_LEVEL,
                "boom_range": Game.Robot.BOOM_RANGE,
                "self_destruction_timeout": Game.Robot.SELF_DESTRUCTION_TIMEOUT,
                "minimum_paint_level_for_self_destruction": Game.Robot.PAINT_LEVEL_FOR_SELF_DESTRUCTION,
                "max_robots": self.__max_robots,
                "teams": self.__team_id
            },
            "map": [[block.value for block in line] for line in self.__map],
            "robots": {
                team: [
                    {
                        "row": robot._row,
                        "col": robot._col,
                        "paint": robot._paint,
                        "uid": robot._uid
                    } if robot is not None else None for robot in robots
                ] for team, robots in self.__robots.items()
            },
            "last_events": self.__last_events,
            "scores": self.__scores
        }


if __name__ == "__main__":
    # Test game init
    print(Game.Block("#"), Game.Block(" "))
    print(" ".join(str(Game.Block(i)) for i in range(1, 9)))
    params = GameParams(map_file="test_maps/small_2p.txt",
                        team_count=2,
                        max_paint_level=10,
                        max_robots=3,
                        round_count=50,
                        boom_range=2,
                        boom_timeout=2,
                        min_paint_for_boom=2)
    g = Game(["Foo"], params)
    print(" ".join(str(Game.Robot(i, 4, 4, g)) for i in range(1, 9)))
    g = Game(["Foo", "Bar"], params)
    print(g)

    # Test Robot placements
    try:
        g.add_robot("Foo", 2, 2)
        print("[OK]")
    except ValueError as e:
        print("[NOK]", e)
    try:
        g.add_robot("Bar", 3, 17)
        print("[OK]")
    except ValueError as e:
        print("[NOK]", e)
    try:
        g.add_robot("Bar", 3, 16)
        print("[OK]")
    except ValueError as e:
        print("[NOK]", e)
    try:
        g.add_robot("Bar", 3, 10)
        print("[NOK]")
    except ValueError as e:
        print("[OK]", e)
    try:
        g.add_robot("Bar", 2, 17, 0)
    except ValueError as e:
        print("[OK]", e)
    try:
        g.add_robot("Bar", 2, 17)
        print("[NOK]")
    except ValueError as e:
        print("[OK]", e)
    try:
        g.add_robot("Bar", 2, 17, 4)
        print("[NOK]")
    except ValueError as e:
        print("[OK]", e)
    print(g)

    # Test movements
    for _ in range(5):
        g.make_turn({
            "Foo": {
                0: Game.Robot.Action.DOWN
            },
            "Bar": {
                0: Game.Robot.Action.LEFT,
                1: Game.Robot.Action.LEFT
            }
        }, {})
        print(g)
    g.make_turn({
        "Foo": {
            0: Game.Robot.Action.BOOM
        },
        "Bar": {
            0: Game.Robot.Action.BOOM,
            1: Game.Robot.Action.BOOM
        }
    }, {})
    print(g)
    for _ in range(3):
        g.make_turn({}, {})
        print(g)

    print(g.get_state_json())
    with open("test_maps/example_state.json", "w") as f:
        json.dump(g.get_state_json(), f, indent=2)
