class Person:
    _name = "Anonymus"
    _chitchat = False

    def __init__(self, name:str, chitchat = False) -> None:
        self._name = name
        self._chitchat = chitchat
    
    def __str__(self) -> str:
        return self._name