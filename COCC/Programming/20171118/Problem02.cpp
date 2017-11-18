/*
 * Ask for a number, and print out the positive integers in increasing order until that number
 */

#include <iostream>
using namespace std;

// Martina asks for numbers on the input, until a positive integer is given, and returns that one
int Martina()
{
    int n;
    cin>>n;

    while (n < 1)
    {
        cout << "Not a positive integer, try again.... pleaaaase. ";
        cin >>n;
    }
    return n;
}

// Michael takes a positive integer, and prints out the positive integers until that number in increasing order
void Michael(int n)
{
    for(int x=0; x<n; x++)
        cout<<x+1<<" ";
    cout<<endl;
}

int main()
{
    
    int number;
    number=Martina();    
    Michael(number);
    
    return 0;
}
