/*
 * Print out the Fibonacci numbers until 1000
 */

#include <iostream>
using namespace std;

int main()
{
    int last;
    int current;
    int next;
    last=1;
    current=1;
    
    cout<<last<<" ";

    while(current<1000)
    {
        cout<<current<<" ";

        next=last+current;
        last=current;
        current=next;
    }

    cout<<endl;
    
    return 0;
}
