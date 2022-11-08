import json

user_file = "users.json"

def read_users_from_json():
    with open(user_file) as f:
        return json.load(f)

def persist_users_to_json(users):
    with open(user_file, "w") as f:
        json.dump(users,f)


def is_valid_user(username, password):
    users = read_users_from_json()
    if username in users:
        if users[username]["password"] == password:
            return {**users[username], "username" : username}

def update_password(username, new_password):
    users = read_users_from_json()
    users[username]["password"]=new_password
    persist_users_to_json(users)
