""" EN 

Implement the `Polynomial_function` class in such a way, that the following code will behave correctly.

"""

""" DE

Implementiere die Klasse `Polynomial_function` so, dass der folgende Code korrekt funktioniert.

"""

class Polynomial_function:
  pass

f = Polynomial_function(name="f")
# For now, this represents the function f(x) = 0
print(f)
# The output shoud be f(x) = 0

f.add_component(coefficient = 3, degree = 2)
# this adds 3*x^2 to the function definition
print(f)
# f(x) = 3*x^2

f.add_component(1,2)
f.add_component(-2,1)
f.add_component(42,0)
print(f)
# f(x) = 4 * x^2 - 2 * x + 42

print(f.value_at(0)) 
# 42
# because f(0) = 4 * 0^2 - 2 * 0 + 42 = 42
print(f.value_at(1))
# 44
print(f.value_at(0.1))
# 41.84



""" EN 
The outputs of print statements can be little different, e.g., instead of `x^2-3*x` it is fine to have `1 * x^2 + (-3) * x + 0` as well. 


Bonus task 1:

Make the following operations work too:
  - `f *= number` - all coefficients are multiplied, similarly do `/=`
  - `f = g + h` - adding together two polynomials, similarly implement  `-`, `*`

Bonus task 2:  
  - `f.derivate()` - apply derivation and return it as a new polynomial
  - `f.of(g)` - return the function `f(g(x))`

"""

""" DE
Die Ausgaben der print-Anweisungen können etwas unterschiedlich sein; statt `x^2-3*x` ist z. B. auch `1 * x^2 + (-3) * x + 0` in Ordnung.


Bonusaufgabe 1:
Sorge dafür, dass auch folgende Operationen funktionieren:
  - `f *= number` - alle Koeffizienten werden multipliziert, analog auch `/=`
  - `f = g + h` - zwei Polynome addieren, analog auch `-`, `*` implementieren

Bonusaufgabe 2:
  - `f.derivate()` - leite das Polynom ab und gib es als neues Polynom zurück
  - `f.of(g)` - gib die Funktion `f(g(x))` zurück

"""