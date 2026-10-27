""" EN
`measurements.json` contains pressure measurements from the same device made 30 seconds apart.

However, some of the readings are incorrect due to outside factors.
We know that the pressure cannot change more than 20.0 in 30 seconds. 
If a jump in values is larger than that, it is considered an outlier.

Example: `[12.3, 18.4, 30.3, 55.5, 39.9]`, the value `55.5` is a false read.

Base task

Write a program, that prints out the total number of outlier values, their indices, and the values themselves.
You can assume, that the first value is not an outlier, and there are no 2 consecutive outlier values.

Bonus 1:

"Repair" the dataset by replacing the outlier values with the average of the neighbor (correct) values. You can assume, that the last value is also a correct measurement.

Bonus 2

Several consecutive values may be outliers.


The provided JSON file has no outliers, you can freely edit it, to test your program.

"""

""" DE
`measurements.json` enthält Druckmessungen desselben Geräts, die im Abstand von 30 Sekunden aufgenommen wurden.

Einige Messwerte sind jedoch aufgrund äußerer Einflüsse fehlerhaft.
Wir wissen, dass sich der Druck in 30 Sekunden nicht um mehr als 20.0 ändern kann.
Wenn ein Sprung zwischen zwei Werten größer ist, gilt der Wert als Ausreißer.

Beispiel: `[12.3, 18.4, 30.3, 55.5, 39.9]`, der Wert `55.5` ist ein fehlerhafter Messwert.

Grundaufgabe:

Schreibe ein Programm, das die Gesamtzahl der Ausreißer, ihre Indizes und die Werte selbst ausgibt.
Du kannst davon ausgehen, dass der erste Wert kein Ausreißer ist und dass es keine 2 aufeinanderfolgenden Ausreißer gibt.

Bonus 1:

"Repariere" den Datensatz, indem du die Ausreißer durch den Durchschnitt der benachbarten (korrekten) Werte ersetzt.
Du kannst davon ausgehen, dass auch der letzte Wert eine korrekte Messung ist.

Bonus 2

Mehrere aufeinanderfolgende Werte können Ausreißer sein.


Die bereitgestellte JSON-Datei enthält keine Ausreißer. Du kannst sie zum Testen deines Programms frei bearbeiten.

"""

