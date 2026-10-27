"""
    In einer Liste werden Log-Einträge, bestehend aus Status und IP-Adresse (durch Doppelpunkt ':' getrennt) gespeichert. 
        Beispiel:
            "OK:127.0.0.1"
            "ERROR:192.168.1.0"

    Implementieren Sie die folgende Funktionen:

    get_error_count:
        Ermitteln Sie die Gesamtzahl der Einträge mit dem Status "ERROR".
        - Parameter:
          logs: Liste mit Log-Einträgen (Liste von Strings)
        - Rückgabewert: 
          Anzahl (int) 

    get_error_ips:
        Ermitteln Sie die IP-Adressen aller Einträge in der Liste mit dem Status "ERROR".
        Eine IP-Adresse soll nur einmal in der Ergebnisliste vorkommen, auch wenn mehrere Einträge derselben IP-Adresse vorhanden sind.
        - Parameter:
            logs: Liste mit Log-Einträgen (Liste von Strings)
        - Rückgabewert: 
            Liste von IP-Adressen (Liste von strings) 
                Beispiel:
                ["192.168.1.10", "192.168.1.0"]
"""

def get_error_count(logs: list[str]) -> int:
    pass

def get_error_ips(logs: list[str]) -> list[str]:
    pass


logs = [
    "OK:192.168.1.0",
    "ERROR:192.168.1.15",
    "OK:192.168.1.10",
    "ERROR:192.168.1.15",
    "ERROR:127.0.0.1",
    "OK:192.168.1.0",
    "ERROR:192.168.0.1"
]

print("Number of errors:", get_error_count(logs))
print("IPs with errors:", get_error_ips(logs))

"""
Erwarteter Output:

    Number of errors: 4
    IPs with errors: ["192.168.1.15", "127.0.0.1", "192.168.0.1"]

"""