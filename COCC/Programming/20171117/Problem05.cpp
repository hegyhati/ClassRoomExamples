/*
 * Ask for 5 real numbers, print out their average, maximum, and minimum.
 *
 *
 */

#include <iostream>
using namespace std;

#define COUNT 5

int main()
{
    double p[COUNT];

    for(int i=0; i<COUNT; i++)
    {
        cin>>p[i];
    }

    double sum=0;
    for(int i=0; i<COUNT; i++)
    {
        sum=sum+p[i];
    }
    cout<<"The average is: "<<sum/COUNT<<endl;

    double min = p[0];
    double max = p[0];
    for(int i=0; i<COUNT; i++)
    {
        if(p[i]<min)
        {
            min=p[i];
        }
        if(p[i]>max)
        {
            max=p[i];
        }
    }
    cout<<"The minimum is: "<<min<<endl;
    cout<<"The maximum is: "<<max<<endl;
    

    
    
    return 0;
}
