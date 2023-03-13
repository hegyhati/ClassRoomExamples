class Character:
    """Represents a character in our game with name, health and damage.
    """
    _name = ''
    _health = 0
    _damage = 0

    def __init__(self, name:str, health:int, damage:int) -> None:
        self._name = name
        self._health = health
        self._damage = damage
        self.__check_dead()

    def __str__(self) -> str:
        return f"{self._name} (HP: {self._health}, DMG: {self._damage})"

    def __check_dead(self) -> None:
        if self._health < 0:
            self._health = 0
    
    def is_alive(self) -> bool:
        """Returns wether the character is still alive or not.

        Returns:
            bool: True if the character is alive, False otherwise
        """
        return self._health > 0

    def attack(self, defender : 'Character') -> None:
        """Attacks the defender if attacker is still alive, and reduces its health by the damage. Prints an error message if not.

        Args:
            defender (Character): tha attacked character
        """
        if self.is_alive():
            print(f"{self} attacks {defender} and makes {self._damage} damage")
            defender._health -= self._damage  
            defender.__check_dead()
        else:
            print(f"{self} cannot attack, because pepsi")