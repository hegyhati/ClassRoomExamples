#ifndef SWORD_HPP
#define SWORD_HPP

#include <string>

class Sword{
    public:
        Sword(int dmg, int dur, double weight=1);
        int use();
        std::string toString() const;
        double getWeight() const;
    private:
        const int dmg;
        int durability;
        const double weight;
};


#endif
