"""
    Implementieren Sie die Klasse ArithmeticSequence und ihre Methoden
    wie angegeben.

    Eine arithmetische Folge wird nach folgender Formel berechnet:

        a(n) = start_value + n * difference

    Beispiel:
        start_value = 5
        difference = 5

        Ergebnisse:
            a(0) = 5
            a(1) = 10
            a(2) = 15
            a(3) = 20
            usw.

    Attribute:
    - start_value:
        Startwert der Folge
    - difference:
        Differenz zwischen zwei aufeinanderfolgenden Werten

    Konstruktor:
    __init__

    Methode:
    get_result:
        * Überprüfung: n >= 0
        * Ist n < 0, soll None zurückgegeben werden.
        * Berechnet den Wert der Folge an der Position n.
        - Parameter:
            Position n (int)
        - Rückgabewert:
            Ergebnis (int)
"""

class ArithmeticSequence:
    __start_value: int
    __difference: int

    def __init__(self, start_value: int, difference: int):
        pass

    def get_result(self, n: int) -> int | None:
        pass


sequence_1 = ArithmeticSequence(5, 5)

values = [0, 1, 2, -1, 10]

for n in values:
    print(f"a({n}): {sequence_1.get_result(n)}")

"""
Erwarteter Output:

    a(0): 5
    a(1): 10
    a(2): 15
    a(-1): None
    a(10): 55
"""
