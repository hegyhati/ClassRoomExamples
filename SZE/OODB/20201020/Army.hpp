#ifndef ARMY_HPP
#define ARMY_HPP

#include "Warrior.hpp"

struct WLI {
    Warrior warrior;
    WLI* next;
}; 

class Army {
    public:
        Army();
        void enlist(Warrior warrior);
        bool dismiss(int position);
        int headcount() const;
        Warrior getWarrior(int position) const;

    private:
        WLI* warriors;

        bool isGoodPosition(int position) const;
        WLI* getWLItem(int position) const;
};

#endif
