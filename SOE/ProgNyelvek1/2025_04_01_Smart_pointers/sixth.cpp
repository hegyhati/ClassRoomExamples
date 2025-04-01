#include <memory>
#include <iostream>
using namespace std;

int main() {
    unique_ptr<int> foo = make_unique<int>(33);
    cout << *foo << endl;
    unique_ptr<int> foo2 = move(foo);
    if (foo) cout << *foo << endl;
    if (foo2) cout << *foo2 << endl;
}