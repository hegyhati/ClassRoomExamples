"""
    Überprüfen Sie, ob eine gegebene Zahl in der Fibonacci-Folge vorkommt (Funktion is_fibonacci). 
        Fibonacci-Folge: 0, 1, 1, 2, 3, 5, 8, 13, ... usw.

        Regeln zur Berechnung der Fibonacci-Folge:
        F(0) = 0 ... Sonderfall
        F(1) = 1 ... Sonderfall
        F(n) = F(n-1) + F(n-2) ... für n >= 2

        Beispiele:
        1  -> True
        5  -> True
        10 -> False
        13 -> True

    Parameter:
        number: Zu überprüfende Zahl, number >= 0
        ValueError, wenn number < 0
    Rückgabewert:
        True, wenn die Zahl in der Fibonacci-Folge vorkommt
        False, wenn die Zahl nicht in der Fibonacci-Folge vorkommt
"""

def is_fibonacci(number: int) -> bool:
    pass

numbers = [0, 1, 4, 21, 143, 610]

for number in numbers:
    print(f"{number}: {is_fibonacci(number)}")

"""
Erwarteter Output:

    0: True
    1: True
    4: False
    21: True
    143: False
    610: True
"""