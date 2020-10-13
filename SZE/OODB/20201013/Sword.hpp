#ifndef SWORD_HPP
#define SWORD_HPP

class Sword{
    public:
        Sword(int dmg, int dur);
        int use();
    private:
        const int dmg;
        int durability;
};


#endif
