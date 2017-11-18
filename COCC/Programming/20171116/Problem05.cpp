/*
 * Ask for a number, and print out the positive integers until that number in increasing order
 * It can be assumed, that the given number is a positive integer.
 *
 * Example:
 * 5 -> 1 2 3 4 5
 */

#include <iostream>
using namespace std;

int main()
{
    int n;
    int x;

    cin>>n;
    
    x=1;
    while(x<=n)
    {
        cout<<x<<" ";
        x=x+1;
    }

    cout<<endl;
    
    return 0;
}
