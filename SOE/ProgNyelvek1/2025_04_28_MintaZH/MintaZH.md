# Programozasi nyelvek 1 - Minta ZH
2025.04.28.

## Igaz-hamis
 - C-ben minden argumentum ertek szerint adodik at.
 - C++ -ban a `struct`-ok nem tartalmazhatnak metodusokat.
 - Java-ban es Pythonban minden sajat osztalynak pontosan egy szuloje van.
 - `const` referenciakent megkapott objektumrol nem keszulhet masolat.
 - C++ -ban egy `const int*` tipusu pointerrel atallithato uj cimre.
 - Ha egy fuggvenyben `new` / `malloc` -kal allokalunk egy valtozot, akkor az a fuggveny vegen automatikusan felszabadul.
 - Pythonban az integer objektumok is referencia-szamlalt objektumok.
 - C++ -ban a template-ek forditasi idoben generalnak uj kodot.

## Stack vs. Heap
Az alabbiak kozul melyik kod allokal a heap-en, es melyik a stack-en?

```python
my_list:int = [1,2,3,4]
```

```js
let myList = [1,2,3,4]
```

```c
int myList[4] = {1,2,3,4};
```

```cpp
std::array<int, 4> myList{1,2,3,4};
```

```cpp
std::vector<int> mylist{1,2,3,4};
```

## Output

Mi a ket kod kimenete?

```python
def foo(l:list[int]) -> None:
    l.append(0)
    print(l)
l = []
foo(l)
foo(l)
foo(l)
```

```cpp
auto foo(std::vector<int> l) -> void {
    l.push_back(0);
    for (int x: l) std::cout << x;
    std::cout << std::endl;
}
std::vector<int> l;
foo(l);
foo(l);
foo(l);
```

## Python under the hood

Melyik C kod irja le leginkabb, ami ebben a Python kodban tortenik, a tobbi miert nem, es mik a kimenetek?

```python
a:int = 3333
b:int = a
a:int = 4444
print(a,b)
```

V1:
```c
int a = 3333;
int b = a;
a = 4444;
printf("%d, %d\n", a, b);
```

V2:
```c
int *a = (int*) malloc(sizeof(int));
*a = 3333;
int *b = a;
*a = 4444;
printf("%d, %d\n", *a, *b);
```

V3:
```c
int *a = (int*) malloc(sizeof(int));
*a = 3333;
int *b = a;
a = (int*) malloc(sizeof(int));
*a = 4444;
printf("%d, %d\n", *a, *b);
```

V4:
```c
const int* new_int(int value) {
    int *tmp = (int*) malloc(sizeof(int));
    *tmp = value;
    return tmp;
}
const int *a = new_int(3333);
const int *b = a;
a = new_int(4444);
printf("%d, %d\n", *a, *b);
```

## Rule of 3/5/0

Sajat szavaiddal fogalmazd meg.

## Copies and copies

Hanyszor (es mikor) hivodik meg az `Point` osztaly copy constructora / assignment operatora az alabbi kod lefutasakor? Hol optimalizalhat a fordito move szemantikaval?

```cpp

struct Point {
    float x;
    float y;
}

class Line {
    Point a;
    Point b;
public:
    Line(Point a, Point b) : a(a), b(b) {}
    float length() {
        return std::sqrt(std::pow(b.x - a.x, 2) + std::pow(b.y - a.y, 2));
    }
}

int main() {
    Point A{1,2};
    Point B{4,5};
    Point C{6,7};
    std::array<Point,3> triangle{Line(A,B), Line(B,C), Line(C,A)};
    float s = 0;
    for(auto line: triangle) s += line.length();
    s /= 2;
    float area = std::sqrt(s);
    for(auto line: triangle) area *= std::sqrt(s-line.length());
    std::cout << "Area of the triangle: " << area;
    return 0;    
}
```

Mikent lehetne a felesleges masolasokat elkrulni?

## Polymorphism

Mit irnak ki az alabbi kodok?

```python
class A:
    def foo(self): print("Afoo")
    def bar(self): self.foo(); print("Abar")

class B(A):
    def foo(self): print("Bfoo")

class C(B):
    def bar(self): print("Cbar"); super().bar()

a:A = C()
a.foo()
a.bar()
```

```cpp
struct A {
    void foo() { std::cout << "Afoo\n"; }
    void bar() { foo(); std::cout << "Abar\n"; }
};

struct B : A {
    void foo() { std::cout << "Bfoo\n"; }
};

struct C : B {
    void bar() { std::cout << "Cbar\n"; B::bar();}
};

int main() {
    A* a = new C();
    a->foo();
    a->bar();
}
```

