#ifndef TOWER_HPP
#define TOWER_HPP


class Tower {
        int x;
        int y;
        double r;
        double dmg;
        int * meh;
    public:
        Tower(int x, int y, double r, double dmg);
        Tower(const Tower& othertower);
        ~Tower();
        void testPrint();
        void setMeh(int mehehe);
};



#endif
