"""
    Implementieren Sie eine Funktion, die Kontobewegungen aus einer JSON-Datei einliest und daraus den aktuellen Kontostand berechnet.

    Jede Kontobewegung besitzt folgende Eigenschaften:
        - id: Eindeutige Nummer
        - type: Art (Einzahlung (=deposit) oder Auszahlung (=withdrawal))
        - amount: Betrag 
        - status: Status der Ein- oder Auszahlung (accepted oder declined) 

    Die JSON-Datei enthält eine Liste 20 Kontobewegungen (als Dictionary Einträge). 

    Regeln zur Berechnung:
    - accepted: Die Kontobewegung wird berücksichtigt.
    - declined: Die Kontobewegung wird ignoriert.
    - deposit: Der Betrag wird zum Kontostand addiert.
    - withdrawal: Der Betrag wird vom Kontostand abgezogen.
  
    Der Kontostand beträgt zu Beginn 0 Euro.

    Implementieren Sie folgende Funktion:

    calculate_balance:
        Liest die Daten aus der JSON-Datei ein und berechnet den aktuellen Kontostand basierend auf den Daten in der Datei. 
        Parameter:
            transactions_json (Name der JSON-Datei)
        Rückgabewert:
            Kontostand (float)
"""

def calculate_balance(transactions_json: str) -> float:
    pass

print(f"Current balance: {calculate_balance("transactions.json")} EUR")

"""
Erwarteter Output:

    Current balance: 1155.78 EUR
"""