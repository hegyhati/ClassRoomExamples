/*
 * Ask for a number, print out if it is prime or not
 * It can be assumed, that the number is positive integer.
 *
 * Examples:
 * 2 -> Prime
 * 6 -> Not prime
 * 12 -> Not prime 
 * 17 -> Prime
 * 1024 -> Not Prime
 *
 */

#include <iostream>
using namespace std;

int main()
{
    int n;
    int x;
    int factors;

    cin >> n;

    factors=0;
    x=1;
    while (x<=n)
    {
        if(n%x==0)
        {
            factors=factors+1;
        }
        x=x+1;
    }

    if(factors==2)
    {
        cout<<"Prime";
    }
    else
    {
        cout<<"Not prime";
    }
    
    cout<<endl;
    
    return 0;
}
