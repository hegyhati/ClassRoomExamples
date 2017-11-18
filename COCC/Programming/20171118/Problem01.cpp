/*
 * Ask for a number from the input, and display Pascals triangle with that depth.
 */

#include <iostream>
#include <iomanip>
using namespace std;


// Marina take a number, and returns its factorial
int Marina(int number)
{
    int fact=1;
    for(int x=1;x<=number;x++)
        fact *=  x;
    return fact;
}

// Mira takes two numbers, and returns top over bottom
int Mira(int top, int bottom)
{
    return Marina(top) / (Marina(bottom) * Marina(top-bottom));
}

int main()
{
    int n;
    cin>>n;
    
    for(int row=0;row<n;row++)
    {
        for(int column=0; column<n-row; column++)
        {
            cout<<setw(4)<<Mira(row+column,row);
        }
        cout<<endl;
    }
    
    return 0;
}
