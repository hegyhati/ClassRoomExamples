#include <iostream>
#include <iomanip>
using namespace std;


int Martina()
{
    int n;
    
    do
    {
        cin >>n;
    }
    while (n < 1);
    
    return n;
}

void Michael(int n)
{
    for(int x=0; x<n; x++)
        cout<<x+1<<" ";
    cout<<endl;
}

int main()
{
     
    Michael(Martina());
    
    return 0;
}
