#ifndef SPELLBOOK_HPP
#define SPELLBOOK_HPP

#include "Item.hpp"
#include <vector>
#include <algorithm>
#include <string>

class SpellBook : public Item {
  public:
    using Spell=std::string;

    SpellBook(unsigned int pagecount) : Item(1.0), pagecount(pagecount) {}

    std::vector<Spell> getSpells() const {return spells;}

    void writeSpell(const Spell& spell) {
      if(std::find(spells.begin(),spells.end(),spell)==spells.end() && spells.size()<pagecount)
        spells.push_back(spell);
    }

    std::string toString() const override {
      std::string toReturn="SpellBook:";
      for (auto spell: spells)
        toReturn+=" "+spell;
      return toReturn;
    }
    
    SpellBook& operator << (const Spell& spell){ 
      writeSpell(spell);
      return *this;
    }

    friend SpellBook& operator >> (const SpellBook::Spell& spell, SpellBook& book) {
      return book << spell;
    }

  private:
    const unsigned int pagecount;

    std::vector<Spell> spells;
};






class SpellScroll : public SpellBook {
  public:
    SpellScroll():SpellBook(1){}
};

#endif
