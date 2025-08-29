/* Ask for the weight of the solvent, and the volume of the solute for COUNT number of solutions.
 * Print out the concentration of each of them, and that of the mixture by pouring them together.
 */

#include <iostream>
using namespace std;

#define COUNT 2

struct Solution{
    double solvent_weight; // g
    double solute_volume; // dl
};

double mass_concentration(Solution solution) { // g/dl
    return solution.solvent_weight / solution.solute_volume;
}

struct Solution PourTogether(Solution solutions[]){
    Solution mixture;
    mixture.solvent_weight=0;
    mixture.solute_volume=0;
    for(int x=0; x<COUNT; x++){
        mixture.solvent_weight+=solutions[x].solvent_weight;
        mixture.solute_volume+=solutions[x].solute_volume;
    }
    return mixture;
}

struct Solution inputSolution(){
    struct Solution solution;
    cout<<"Please give the weight of the solvent in gramms: ";
    cin>>solution.solvent_weight;
    cout<<"Please give the volume of the solute volume in deciliters: ";
    cin>>solution.solute_volume;
    cout<<"The mass concentration of the solution is "
        <<mass_concentration(solution)<<" g/dl"<<endl;
    return solution;
}

int main(){
    
    struct Solution mysolutions[COUNT];

    for(int i=0;i<COUNT;i++)
        mysolutions[i]=inputSolution();

    struct Solution mixture=PourTogether(mysolutions);
    cout<<endl<<"The mass_concentration of the mixture is "
        <<mass concentration(mixture)<<" g/dl"<<endl;
    
    return 0;
}
