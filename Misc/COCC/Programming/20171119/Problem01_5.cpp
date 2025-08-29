/* Ask for the width, length, and number of trees of gardens until we run out of them.
 * Print out their total area, and the total number of trees.
 */

#include <iostream>
#include <numeric>
#include <string>
#include <list>
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

bool moreInput(){
    cout<<"Do You have more gardens? ";
    string answer;
    cin>>answer;
    return answer=="yes";
}

int main(){

    list<Garden> mygardens;
    do{
        mygardens.push_back(Garden());
    } while (moreInput());

    cout<<"The total area is: "<<accumulate(mygardens.begin(),mygardens.end(),0,addArea)<<endl;
    cout<<"The total number of trees is: "<<accumulate(mygardens.begin(),mygardens.end(),0,addTrees)<<endl;
    
    return 0;
}
