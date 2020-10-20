#include <iostream>
using namespace std;

#include "Inventory.hpp"
#include "Sword.hpp"

int main(){
    Inventory my_inventory(4);
    if(my_inventory.put(Sword(12,6))) cout<<"Yeppee\n"; else cout << ":-(\n";
    if(my_inventory.put(Sword(23,6))) cout<<"Yeppee\n"; else cout << ":-(\n";
    if(my_inventory.put(Sword(45,5))) cout<<"Yeppee\n"; else cout << ":-(\n";
    if(my_inventory.put(Sword(67,2))) cout<<"Yeppee\n"; else cout << ":-(\n";
    if(my_inventory.put(Sword(35,3))) cout<<"Yeppee\n"; else cout << ":-(\n";
    if(my_inventory.put(Sword(87,5))) cout<<"Yeppee\n"; else cout << ":-(\n";
    
    cout << my_inventory.size() << " db kardunk van.\n";
    for (int i=0; i<my_inventory.size(); i++)
        cout<<" - "<<my_inventory.getSword(i).toString()<<"\n";

    my_inventory.drop(3);
    
    
    cout << my_inventory.size() << " db kardunk van.\n";
    for (int i=0; i<my_inventory.size(); i++)
        cout<<" - "<<my_inventory.getSword(i).toString()<<"\n";

    my_inventory.drop(4);
    
    
    cout << my_inventory.size() << " db kardunk van.\n";
    for (int i=0; i<my_inventory.size(); i++)
        cout<<" - "<<my_inventory.getSword(i).toString()<<"\n";
    
my_inventory.drop(0);
    
    
    cout << my_inventory.size() << " db kardunk van.\n";
    for (int i=0; i<my_inventory.size(); i++)
        cout<<" - "<<my_inventory.getSword(i).toString()<<"\n";
    
my_inventory.drop(0);
    
    
    cout << my_inventory.size() << " db kardunk van.\n";
    for (int i=0; i<my_inventory.size(); i++)
        cout<<" - "<<my_inventory.getSword(i).toString()<<"\n";

    my_inventory.drop(0);
    
    
    cout << my_inventory.size() << " db kardunk van.\n";
    for (int i=0; i<my_inventory.size(); i++)
        cout<<" - "<<my_inventory.getSword(i).toString()<<"\n";

    my_inventory.drop(0);
    
    
    cout << my_inventory.size() << " db kardunk van.\n";
    for (int i=0; i<my_inventory.size(); i++)
        cout<<" - "<<my_inventory.getSword(i).toString()<<"\n";

    my_inventory.drop(0);
    
    
    cout << my_inventory.size() << " db kardunk van.\n";
    for (int i=0; i<my_inventory.size(); i++)
        cout<<" - "<<my_inventory.getSword(i).toString()<<"\n";


    return 0;
}
