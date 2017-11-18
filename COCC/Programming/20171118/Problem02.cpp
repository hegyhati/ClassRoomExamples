#include <iostream>
#include <iomanip>
using namespace std;


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
