#include <iostream>
#include <iomanip>
using namespace std;

int Marina(int number)
{
    int fact=1;
    for(int x=1;x<=number;x++)
        fact *=  x;
    return fact;
}

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
