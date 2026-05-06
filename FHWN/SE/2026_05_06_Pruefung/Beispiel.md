# Software Engineering - Beispiel

### 1. Erklär den Unterschied zwischen Validierung und Verifikation. Was bedeutet es, wenn die Verifikation passt, aber die Validierung fehlschlägt? Bringen Sie ein Beispiel. 

### 2. Nenn die wichtigsten Ideen des Agilen Manifests. 

### 3. Definier die folgenden Konzepte in einem Satz 
  - UML 
  - einen beliebigen Buchstaben aus SOLID 
  - KISS 

### 4. Gib ein kurzes Codebeispiel für das zuvor ausgewählte SOLID-Prinzip.

### 5. Was ist ein häufiger „Konflikt“ zwischen Managern und Ingenieuren, und zu welchen Ergebnissen kann er führen?

### 6. Erzähl in eigenen Worten, was ein Unit-Test ist und warum wir ihn verwenden.

### 7. Gib zwei Beispiele, wofür CI verwendet werden kann.

### 8. Wir haben die folgende Klasse, die ein Defense-System modelliert:

```
                  |       |       |       |
ATTACKER->  AREA0 | AREA1 | AREA2 |  ...  | AREAN+1 US
                  |       |       |       |
                WALL0   WALL1   WALL2   WALLN
```

```py
class Defense_System:
    def __init__(self, number_of_walls:int) -> None: ...
    def destroy_wall(self, wall_index:int) -> None: ...
    def is_area_breached(self,area_idx:int) -> bool: ...
    def are_we_breached(self) -> bool:...
```

Welche Unit-Tests können für diese Klasse implementiert werden? (Mind. 3)

### 9. Wahr/Falsch

 - `git commit` arbeitet immer auf dem `master`-/`main`-Branch.
 - Docker ist eine Virtual-Machine-Engine.
 - Ein Pull Request kann nur einen Reviewer haben.