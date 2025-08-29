/*
 * Print out the even numbers from 100 to 0
 */

#include <iostream>
using namespace std;

int main()
{
    int n;
    n=100;

    while(n>=0)
    {
        if (n%2==0)
        {
            cout<<n<<" ";
        }
        n=n-1;
    }

    cout<<endl;
    
    return 0;
}
