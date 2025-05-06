# Programozasi nyelvek 1 - ZH
2025.05.07.

## Igaz-hamis
 - C-ben egy `struct` merete forditasi idoben ismert.
 - C++ -ban egy `class` akkor `abstract` ha minden fuggvenye `pure virtual`
 - Az `override` kulcsszo megvaltoztatja egy lefordulo kod mukodeset.
 - `const` referenciakent megkapott objektumrol keszulhet masolat.
 - C++ -ban egy `int * const` tipusu pointer atallithato uj cimre.
 - Egy `unique_ptr` minden esetben tartalmaz erteket.
 - `virtual` fuggvenyeknek futasi idoben van overheadje.
 - C++ -ban a template-ek forditasi idoben generalnak uj kodot.

## Stack vs. Heap
Az alabbiak kozul melyik kod allokal a heap-en, es melyik a stack-en?

```python
foo:int = 3
```

```js
let foo = 3
```

```c
int foo = 3;
```

```cpp
std::unique_ptr<int> foo = std::make_unique<int>(3);
```

## Output

Mi a ket kod kimenete?

```cpp
#include <iostream>
using std::cout

struct Parent {
    void foo() { cout << "PF\n"; }
    virtual void bar() { cout << "PB\n"; foo();  }
};

struct Derived : public Parent {
    void foo() override { cout << "DF\n"; }
};

int main() {
    Parent().bar();
    Derived().bar();
    return 0;
}
```

```python
class Parent:
    def foo(self): print("PF")
    def bar(self): print("PB"), self.foo() 

class Derived(Parent):
    def foo(self): print("DF")

Parent().bar()
Derived().bar()
```


## Python under the hood

Melyik C kod irja le leginkabb, ami ebben a Python kodban tortenik, miert, es mik a kimenetek?

```python
def foo(l:list[int])
    for x in l:
        x = 2
my_list:list[int] = [1,2,3]
foo(my_list)
print(my_list)
```

V1:
```c
void foo(int* list, int size) {
    for (int i=0; i<size; ++i)
        list[i] = 2;
}
int myList[] = {1,2,3};
foo(myList, 3);
magic_print(myList);
```

V2:
```c++
void foo(array<int, 3> list) {
    for (int i=0; i<3; ++i)
        list[i] = 2;
}
array<int,3> myList = {1,2,3};
foo(myList);
magic_print(myList);
```

V3:
```c++
void foo(vector<int> list) {
    for (auto x: list)
        x = 2;
}
vector<int> myList = {1,2,3};
foo(myList);
magic_print(myList);

V4:
```c++
void foo(vector<int>& list) {
    for (auto& x: list)
        x = 2;
}
vector<int> myList = {1,2,3};
foo(myList);
magic_print(myList);

V5:
```c++
void foo(shared_ptr<vector<int>> list) {
    for (auto x: list)
        x = 2;
}

auto myList = make_shared<vector<int>>{1,2,3};
foo(myList);
magic_print(myList);
```

Ha meg kozelebbi ekvivalens kodot tudnal adni, ird fel.

## `Const`, `override`

Sajat szavaiddal fogalmazd meg mire jok ezek, miert erdemes hasznalni, mikor.

## Constructors

Az alabbi kod lefutasakor mikor, milyen sorrendben melyik osztalynak hajtodnak vegre alapertelmezett, parameteres, masolo, move, copy konstruktorai, destruktorai, move / copy assignmentjei. (Feltehetjuk, hogy a megadott kodokon kivul ezek mindegyike rendelkezesre all, a deklaralt metodusok megfeleloen implementalva vannak, stb.)

```cpp
enum Direction {UP, LEFT, DOWN, RIGHT};

struct ChessField {
    char column;
    uint row;
    ChessField neighbor(Direction) const;
};

enum Color {WHITE, BLACK};

struct ChessPiece {
    ChessField position;
    Color color;
    ChessPiece(ChessField pos, Color c) : position(pos), color(col) {}
    virtual vector<ChessField> nextFields() const  = 0;
    bool canMove(ChessField pos) const;
}

struct Rook : public ChessPiece {
    Rook(ChessField pos, Color color) : ChessPiece(pos, color) {}
    vector<ChessField> nextFields() const override;
};

// Similar code for other pieces

int main() {
    Rook r1(ChessField{"A",1}, WHITE);
    Knight k1 = Kinght(ChessField{"A",2}, BLACK);
    Bishop b1;
    b1 = Bishop(ChessField{"A",3}, WHITE);
    
    vector<ChessPiece*> pieces;
    pieces.push_back(&r1);
    pieces.push_back(&k1);
    pieces.push_back(&b1);

    for (const auto piece : pieces) {
        for (const auto field : piece->nextFields()) {
            bool canMove = true;
            for (const auto piece2 : pieces) {
                if (piece2.position == field && piece.color == piece2.color) canMove = false;
            }
            cout << "Piece can move to: " << field.column << field.row << "\n";
        }
    }
}



```

Mikent lehetne a felesleges masolasokat elkrulni?

