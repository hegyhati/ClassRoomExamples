/*
 * Ask for two numbers
 * Print out the rectangle from + symbols with the width and depth as those numbers
 * The inside of the rectangle should be empty (spaces)
 * It can be assumed, that the numbers are positive integers larger than 2.
 *
 * Example:
 * 5 6 -> +++++
 *        +   +
 *        +   +
 *        +   +
 *        +   +
 *        +++++
 *
 */

#include <iostream>
using namespace std;

int main()
{
    int width;
    int height;

    cin>>width;
    cin>>height;

    for(int column=1; column<=width; column++)
    {
        cout<<"+";
    }
    cout<<endl;
    
    for(int row=1; row<=height-2; row++)
    {
        cout<<"+";
        for(int column=1; column<=width-2; column++)
        {
            cout<<" ";
        }
        cout<<"+";
        cout<<endl;
    }

    for(int column=1; column<=width; column++)
    {
        cout<<"+";
    }
    cout<<endl;
    
    return 0;
}
