#ifndef KONYV_H
#define KONYV_H

#include <string>
#include <iostream>

class Konyv{
  protected:
    std::string szerzo;
    std::string cim;
    int ev;
  public:
    Konyv(std::string szerzo, std::string cim, int ev)
      :szerzo(szerzo),cim(cim),ev(ev) {}
    virtual ~Konyv(){}
    std::string getSzerzo() const {return szerzo;}
    std::string getCim() const {return cim;}
    int getEv() const {return ev;}
    virtual std::string toString() const {return szerzo + " - " + cim + " ("+std::to_string(ev)+")";}

    /* Plusz pontokert */
    bool operator<(const Konyv& other) const;
    
};

std::ostream& operator << (std::ostream& s, const Konyv& k);
 

#endif
