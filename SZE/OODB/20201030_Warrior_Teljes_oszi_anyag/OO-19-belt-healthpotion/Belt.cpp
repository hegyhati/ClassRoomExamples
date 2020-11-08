#include "Belt.hpp"

Belt::Belt() : potions(nullptr) {}

Belt::~Belt() { clear(); }

int Belt::count() const {
  int count=0;  
  for(BeltItem* tmp=potions;tmp!=nullptr; tmp=tmp->next) count++;
  return count;
}

void Belt::put(const HealthPotion& potion) { 
  potions = new BeltItem{potion,potions};
}

const HealthPotion& Belt::watch(int index) const {
  checkIndex(index);
  BeltItem* tmp;
  for(tmp=potions;index>0;--index) tmp=tmp->next;
  return tmp->potion;
}

HealthPotion Belt::get(int index) {
  checkIndex(index);
  BeltItem** tmp;
  for(tmp=&potions;index>0;--index) tmp=&((*tmp)->next);
  HealthPotion toReturn = (*tmp)->potion;
  BeltItem* toDelete=(*tmp);
  (*tmp) = (*tmp)->next;
  delete toDelete;
  return toReturn;
}

void Belt::clear(){
  while(count()>0) get(0);
}

void Belt::checkIndex(int index) const {
  if (index<0 || index>=count()) throw WrongIndexException();
}
