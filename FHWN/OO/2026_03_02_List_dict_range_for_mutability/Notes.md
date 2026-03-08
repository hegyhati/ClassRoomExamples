# Python Grundlagen 2

## Funktionen

Funktionen haben wir in C schon verwendet. 
Es gibt eigentlich (mindestens) zwei wichtige Gründe, warum es gut ist, Code in mehrere Funktionen aufzuteilen:
 - Vermeidung der Codewiederholungen.
 - Aufteilung des Codes in kleinere Teile, die unabhängig entwickelt, überprüft und getestet werden können.

Beide sind nützlich, um das Fehlerrisiko zu minimieren.

Hier gibt es einige einfache Funktionen mit C-Äquivalenten:

<table><tr><th style="width: 50%;">C</th><th style="width: 50%;">Python</th></tr><tr><td style="vertical-align: top;">

```c
int smaller(int num1, int num2) {
    return num1 < num2 ? num1 : num 2;
}
```

</td><td style="vertical-align: top;">

```python
def smaller(num1,num2):
    return num1 if num1 < num2 else num 2
```

</td></tr><tr><td style="vertical-align: top;">

```c
bool isPrime(int number) {
    int i = 2;
    while (i*i < number) {
        if (number % i == 0)
            return false
        ++i;
    }
    return true;
}
```

</td><td style="vertical-align: top;">

```python
def is_prime(number):
    i = 2
    while i**2 < number:
        if number % i == 0:
            return False
        i += 1
    return True
```

</td></tr><tr><td style="vertical-align: top;">

```c
bool isPerfect(int number) {
    int dividerSum = 0;
    for (int i = 1; i <= number/2; ++i) 
        if (number % i == 1)
            dividerSum += i;
    return number == dividerSum;
}
```

</td><td style="vertical-align: top;">

```python
def is_perfect(number):
    divider_sum = 0
    for i in range(n//2 + 1):
        if number % i == 0:
            divider_sum += i
    return number == divider_sum
```

</td></tr></table>

### Typ


### Pass-by-?

C ist eine Pass-by-Value-Sprache. Das bedeutet, dass wenn eine Variable als Argument an eine Funktion übergeben wird, ihr Wert in einen neuen Speicherbereich der Funktion kopiert wird.
Deshalb ist die Ausgabe dieses Codes 1 und nicht 2:

```c
void makedouble(int x){
    x *= 2;
}

int main() {
    number = 1;
    makedouble(number);
    printf("%d\n", number);
}
```

Die Ausgabe des Python-Äquivalents ist ebenfalls 1:

```py
def makedouble(x)
    x *= 2

number = 1
makedouble(number)
print(number)

```

Aber was im Hintergrund passiert, ist etwas anderes. Tatsächlich sind alle Variablen in Python Zeiger, also Referenzen.
Wenn eine Variable übergeben wird, wird diese Referenz kopiert und zeigt auf denselben Speicherbereich.
Aber `x *= 2` ist nur `x = x * 2`, bei dem zuerst der neue Wert `x*2` berechnet wird und dann die Referenz `x` auf einen neuen Speicherbereich zeigt, in dem dieser doppelte Wert gespeichert ist.

## `list`

### Operatoren

### Methoden

### `range`, `random.choices`

### (Im)mutability

## `for`-Schleifen

## `dict`

### Operatoren

### Methoden
