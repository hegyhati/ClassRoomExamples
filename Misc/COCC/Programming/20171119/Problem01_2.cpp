/* Ask for the width and length of COUNT number of gardens, and how many trees they have.
 * Print out their total area, and the total number of trees.
 */

#include <iostream>
using namespace std;

#define COUNT 2

struct Garden {
    double width;
    double length;
    int trees;
};

struct Garden Nevine(){
    struct Garden garden;
    cout<<"Please give the width of the next garden: ";
    cin>>garden.width;        
    cout<<"Please give the length of the next garden: ";
    cin>>garden.length;
    cout<<"Please give the number of trees in the next garden: ";
    cin>>garden.trees;

    return garden;
}

double Aziz(struct Garden garden){
    return garden.width*garden.length;
}

double Rebecca (struct Garden gardens[]){
    double totalArea=0;
    for(int x=0;x<COUNT;x++) 
        totalArea += Aziz(gardens[x]);
    return totalArea;
}

double Rania(struct Garden gardens[]){
    double totalTrees=0;
    for(int x=0;x<COUNT;x++) 
        totalTrees += gardens[x].trees;
    return totalTrees;
}

int main(){
    struct Garden mygardens[COUNT];


    for(int x=0;x<COUNT;x++)
        mygardens[x]=Nevine();


    cout<<"The total area is: "<<Rebecca(mygardens)<<endl;
    cout<<"The total number of trees is: "<<Rania(mygardens)<<endl;
    
    return 0;
}
