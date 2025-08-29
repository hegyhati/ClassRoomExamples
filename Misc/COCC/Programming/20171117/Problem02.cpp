/*
 * Ask for two numbers
 * Print out rectangle from + symbols with the width and depth as those numbers
 * It can be assumed, that the numbers are positive integers.
 *
 * Example:
 * 5 6 -> +++++
 *        +++++
 *        +++++
 *        +++++
 *        +++++
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
            cout<<"+";
        }
        cout<<endl;
    }
    
    return 0;
}
