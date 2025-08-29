/*
 * Ask for a number, print out its prime factorization.
 * It can be assumed, that the number is positive integer larger than 2.
 *
 * Examples:
 * 2 -> 2
 * 6 -> 2 3
 * 12 -> 2 2 3 
 * 10 -> 2 5
 * 1024 -> 2 2 2 2 2 2 2 2 2 2
 *
 */

#include <iostream>
using namespace std;

int main()
{
    int n;
    int x;

    cin >> n;

    x=2;
    while (n!=1)
    {
        if(n%x==0)
        {
            cout << x << " ";
            n=n/x;
        }
        else
        {
            x=x+1;
        }
    }

    cout<<endl;
    
    return 0;
}
