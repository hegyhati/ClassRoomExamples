## Motivation

Da uns der Hase aus der vorherigen Aufgabe sehr gefällt, haben wir beschlossen, eine echte Eisenstatue von ihm herzustellen, indem wir die dreieckigen Platten wie im Modell zusammenschweißen.

Leider kann Eisen rosten, und [Rost breitet sich tendenziell aus](https://commandlinux.com/statistics/rust-programming-language-adoption/).

Wenn ein Dreieck rostet, rosten am nächsten Tag auch alle seine Nachbarn (also die Dreiecke, mit denen es eine Kante teilt).

Schreibe ein `main`, das nach dem Index eines Dreiecks im Modell fragt und anschließend:
 - ausgibt, wie viele Tage der Hase benötigt, um vollständig zu rosten, wenn das ausgewählte Dreieck zuerst rostet.
 - für jeden Tag ausgibt, wie viele neue Dreiecke Rost angesetzt haben.

## Zusatzaufgabe 1

Lass `main` zuerst ausgeben, welches Dreieck als "Patient 0" am günstigsten und welches am ungünstigsten ist und wie viele Tage es im jeweiligen Fall dauert.

## Zusatzaufgabe 2

Die Ausbreitungslogik ist anders: Die Zeit, die der Rost benötigt, um sich von einem Dreieck zu einem anderen auszubreiten, ist eine lineare Funktion des Abstands zwischen ihren Schwerpunkten. Gib die Reihenfolge aus, in der die Dreiecke für das vom Benutzer angegebene Startdreieck rosten.

## Code

Du kannst gerne beliebige Datenstrukturen oder Hilfsfunktionen aus Aufgabe 2 wiederverwenden.
