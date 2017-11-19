#include <iostream>
using namespace std;

#define GARDEN 2

int main(){
    double width[GARDEN];
    double length[GARDEN];

    for(int x=0;x<GARDEN;x++){
        cout<<"Please give the width of the "<<x+1<<". garden: ";
        cin>>width[x];        
        cout<<"Please give the length of the "<<x+1<<". garden: ";
        cin>>length[x];
    }

    double totalArea=0;
    for(int x=0;x<GARDEN;x++)
        totalArea += width[x]*length[x];

    cout<<"The total area is: "<<totalArea<<endl;
    
    return 0;
}
