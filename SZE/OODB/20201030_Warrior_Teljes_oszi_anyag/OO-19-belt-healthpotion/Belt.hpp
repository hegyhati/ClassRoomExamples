#ifndef BELT_HPP
#define BELT_HPP

#include "HealthPotion.hpp"

class Belt{
  public:
    class WrongIndexException{};

    Belt();

    Belt(const Belt&) = delete;
    Belt& operator=(const Belt&) = delete;
    ~Belt();

    void put(const HealthPotion& potion);
    HealthPotion get(int slot);
    int count() const;
    const HealthPotion& watch(int slot) const;
    void clear();
  
  private:

    struct BeltItem {
      HealthPotion potion;
      BeltItem* next;
    };
    
    BeltItem* potions;

    void checkIndex(int index) const;
};


 


#endif
