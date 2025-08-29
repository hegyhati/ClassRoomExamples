/*
 * Ask for two numbers, and print out the integers from the smaller one until the bigger one
 *
 * Examples:
 * 4 6 -> 4 5 6
 * 8 2 -> 2 3 4 5 6 7 8
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
    int smaller;
    int bigger;

    cin >> a;
    cin >> b;

    if (a>b)
    {
        bigger=a;
        smaller=b;
    }
    else
    {
        bigger=b;
        smaller=a;
    }

    x=smaller;
    while (x<=bigger)
    {
        cout << x << " ";
        x=x+1;
    }

    cout<<endl;
    
    return 0;
}
