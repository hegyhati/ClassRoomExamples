/*
 * Ask for two numbers, and print out the integers from the first one until the second one
 * It can be assumed, that the first one will not be greater than the second one.
 *
 * Examples:
 * 4 6 -> 4 5 6
 * 2 8 -> 2 3 4 5 6 7 8
 * -5 2 -> -5 -4 -3 -2 -1 0 1 2
 * 6 6 -> 6
 *
 */

#include <iostream>
using namespace std;

int main()
{
    int a;
    int b;
    int x;

    cin >> a;
    cin >> b;

    x=a;
    while (x<=b)
    {
        cout << x << " ";
        x=x+1;
    }

    cout<<endl;
    
    return 0;
}
