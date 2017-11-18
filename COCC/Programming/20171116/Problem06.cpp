/*
 * Ask for a number, and if it is a positive integer, print out the positive integers until that number in increasing order.
 * Otherwise print out "Wrong input"
 *
 * Examples:
 * 5 -> 1 2 3 4 5
 * 3 -> 1 2 3
 * 0 -> Wrong input
 * 1 -> 1
 * -9-> Wrong input
 */

#include <iostream>
using namespace std;

int main()
{
    int n;
    int x;

    cin>>n;

    if(n>=1)
    {
        x=1;
        while(x<=n)
        {
            cout<<x<<" ";
            x=x+1;
        }
    }
    else
    {
        cout<<"Wrong input";
    }

    cout<<endl;
    
    return 0;
}
