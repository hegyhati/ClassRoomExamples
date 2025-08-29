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
    
    for(int row=1; row<=height; row++)
    {
        for(int column=1; column<=width; column++)
        {
            if(row==1 || row==height || column==1 || column==width)
            {
                cout<<"+";
            }
            else
            {
                cout<<" ";
            }
        }
        cout<<endl;
    }
    
    return 0;
}
