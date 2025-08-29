/*
 * Ask for a number until it is a positive integer.
 * Print out the positive integers in increasing order until that number.
 *
 */

#include <iostream>
using namespace std;

int main()
{
    int n;
    int x;

    cin>>n;

    while(n<1)
    {
        cout<<"Wrong input, please enter a positive integer"<<endl;
        cin>>n;        
    }
    
    x=1;
    while(x<=n)
    {
        cout<<x<<" ";
        x=x+1;
    }    

    cout<<endl;
    
    return 0;
}
