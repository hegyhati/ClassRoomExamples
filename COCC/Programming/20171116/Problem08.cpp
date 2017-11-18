/*
 * Ask for two numbers, and print out the bigger one.
 * If they are equal, print out their value.
 *
 */

#include <iostream>
using namespace std;

int main()
{
    int a;
    int b;

    cin >> a;
    cin >> b;

    if (a>b)
    {
        cout << a;
    }
    else
    {
        cout << b;
    }

    cout<<endl;
    
    return 0;
}
