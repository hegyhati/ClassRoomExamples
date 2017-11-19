/* Ask for the width and length of COUNT number of gardens, and how many trees they have.
 * Print out their total area, and the total number of trees.
 */

#include <iostream>
#include <numeric>
using namespace std;

#define COUNT 2

class Garden {
    private:
        double width;
        double length;
        int trees;
    public:
        Garden(){
            cout<<"Please give the width of the next garden: ";
            cin>>width;        
            cout<<"Please give the length of the next garden: ";
            cin>>length;
            cout<<"Please give the number of trees in the next garden: ";
            cin>>trees;
        }

        double getArea(){
            return width*length;
        }

        double getTrees(){
            return trees;
        }
};

double addArea(double x, Garden garden){return x+garden.getArea();}
double addTrees(double x, Garden garden){return x+garden.getTrees();}

int main(){
    
    Garden mygardens[COUNT];

    cout<<"The total area is: "<<accumulate(mygardens,mygardens+COUNT,0,addArea)<<endl;
    cout<<"The total number of trees is: "<<accumulate(mygardens,mygardens+COUNT,0,addTrees)<<endl;
    
    return 0;
}
