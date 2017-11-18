/*
 * Ask for a number, print out the positive integers in a diagonal until that number
 *
 * Example:
 * 5 -> 1
 *       2
 *        3
 *         4
 *          5
 *
 */

#include <iostream>
using namespace std;

int main()
{
    int n;
    cin>>n;

    for(int x=1; x<=n; x++)
    {
        for(int y=1; y<=x-1; y++)
        {
            cout<<" ";
        }
        cout<<x;
        cout<<endl;
    }
    
    return 0;
}
