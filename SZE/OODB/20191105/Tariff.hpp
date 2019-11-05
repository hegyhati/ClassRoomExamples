#ifndef TARIFF_HPP
#define TARIFF_HPP

#include "MonthlyPhoneLog.hpp"

class Tariff {
  public:
    virtual double calculateBill(const MonthlyPhoneLog&) const =0;
    virtual ~Tariff(){}
};


#endif
