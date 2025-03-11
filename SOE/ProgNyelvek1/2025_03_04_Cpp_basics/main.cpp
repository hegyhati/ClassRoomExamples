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

    PrioList pl2(pl);
    pl.push_increasing(45);
    pl.debug_list();
    pl2.debug_list();
    pl2.pop_front();
    pl.debug_list();
    pl2.debug_list();
    


    std::cout<<"\n";
    return 0;    
}