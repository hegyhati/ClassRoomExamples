#ifndef STARIFF_HPP
#define STARIFF_HPP

#include "MonthlyPhoneLog.hpp"
#include "Tariff.hpp"

class SimpleTariff : public Tariff {
    double secondcost; /* HUF/s */
    double smscost; /* HUF/sms */
    int base; /* in seconds */
  public:
    SimpleTariff(double minutecost, double smscost, int base=1);
    virtual double calculateBill(const MonthlyPhoneLog&) const override;
};


#endif
