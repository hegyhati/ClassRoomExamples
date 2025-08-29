/*
 * Print out a 3 by 4 rectangle from + symbols
 *
 */

#include <iostream>
using namespace std;

int main()
{
    for(int row=1; row<=4; row++)
    {
        for(int column=1; column<=3; column++)
        {
            cout<<"+";
        }
        cout<<endl;
    }
    
    return 0;
}
