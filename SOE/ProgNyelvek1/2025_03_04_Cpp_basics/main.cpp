#include <iostream>
#include "priolist.hpp"

int main() {
    PrioList pl;
    int d;
    do {
        std::cout << "Adj egy szamot: ";
        std::cin >> d;
        pl.push_increasing(d);
        pl.debug_list();
    } while (d!=0);

    /*
    while(!pl.is_empty()){
        std::cout << pl.pop_front() << " ";
    }*/

    std::cout<<"\n";
    return 0;    
}