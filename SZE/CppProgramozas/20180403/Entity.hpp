#ifndef ENTITY_HPP
#define ENTITY_HPP

class Entity {
    protected:
        int x;
        int y;
        Entity(int x, int y);
    public:
        double distance(const Entity& other) const;
        bool isPosition(int x, int y) const;
};


#endif
