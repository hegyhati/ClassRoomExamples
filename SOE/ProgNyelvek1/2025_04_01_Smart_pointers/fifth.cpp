#include <memory>
#include <iostream>
using namespace std;

int main() {
    weak_ptr<int> ize;
    {
        shared_ptr<int> bar;
        {
            auto foo = make_shared<int>(3);
            bar = foo;
            ize = foo;
            cout << ize.use_count() << endl;
            cout << *foo << *bar << *ize.lock()<< endl;
        }
        cout << ize.use_count() << endl;
        cout << /* *foo << */ *bar << *ize.lock()<< endl;
    }
    cout << ize.use_count() << endl;
    cout << *ize.lock() << endl; // Segfault, check with expired()


}