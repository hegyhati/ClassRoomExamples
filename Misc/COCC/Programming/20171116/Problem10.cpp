/*
 * Ask for a number, print out its factors.
 * It can be assumed, that the number is positive.
 *
 * Examples:
 * 1 -> 1
 * 2 -> 1 2
 * 6 -> 1 2 3 6
 * 12 -> 1 2 3 4 6 12
 * 10 -> 1 2 5 10
 * 1024 -> 1 2 4 8 16 32 64 128 256 512 1024
 *
 */

#include <iostream>
using namespace std;

int main()
{
    int n;
    int x;

    cin >> n;

    x=1;
    while (x<=n)
    {
        if(n%x==0)
        {
            cout << x << " ";
        }
        x=x+1;
    }

    cout<<endl;
    
    return 0;
}
