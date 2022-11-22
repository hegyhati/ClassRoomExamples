import json

user_file = "users.json"


def read_users_from_json():
    """
    Reads users from database file.

    Returns a dictionary stored within **the** file.
    """
    with open(user_file) as f:
        return json.load(f)

def persist_users_to_json(users):
    """
    Persists the user data stored in `users` to the database file.
    """
    with open(user_file, "w") as f:
        json.dump(users,f)


def fetch_user(username, password):
    """Returns dictionary containing user data.

    Args:
        username (str): the username
        password (str): plain text password

    Returns:
        dict: dictionary containing user data or None
    """
    users = read_users_from_json()
    if username in users:
        if users[username]["password"] == hash(password):
            return {**users[username], "username" : username}

def update_password(username:str, new_password:str) -> None:
    """Updates password for user

    Args:
        username (str): the username
        new_password (str): the new password in plain text
    """
    users = read_users_from_json()
    users[username]["password"]=hash(new_password)
    persist_users_to_json(users)

def hash(input:str) -> str:
    """Simple hash function that returns the first 4 digits with even indices.

    Args:
        input (str): input to be hashed

    Returns:
        str: hashed output

    >>> hash("biztosjelszo")
    'bzoj'
    >>> hash("kiskutya")
    'ksuy'
    >>> hash("aba")
    'aa__'
    """
    return (input[::2]+"___")[:4]

def test_hash():
    print ("hash('biztosjelszo'): ", "OK" if hash("biztosjelszo")=="bzoj" else "ERROR")

if __name__ == "__main__":
    test_hash()