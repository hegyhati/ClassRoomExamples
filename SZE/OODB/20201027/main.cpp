
#include <iostream>
using namespace std;

#include <string>
#include "Warrior.hpp"
#include "List.hpp"

#include <list>

int main(){

    list<int> intlist;

    List<Warrior> list;
    string response;
    while(true){
        cin >> response;
        if (response == "eleg") break;
        int hp;
        int mana;
        cin >> hp >> mana;
        list.put(Warrior(response,hp,mana));
    }

    for(int i=0; i<list.size(); ++i)
        cout << list.getElement(i).toString() << endl;
    
    cout << "Removing 1"<<endl;
    list.remove(1);

    for(int i=0; i<list.size(); ++i)
        cout << list.getElement(i).toString() << endl;
    
    
    cout << "Cleaning"<<endl;
    list.clean();

    for(int i=0; i<list.size(); ++i)
        cout << list.getElement(i).toString() << endl;
    

    cout << endl;
    
}
