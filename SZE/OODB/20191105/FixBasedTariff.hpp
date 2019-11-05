#ifndef FBTARIFF_HPP
#define FBTARIFF_HPP

#include "MonthlyPhoneLog.hpp"
#include "Tariff.hpp"

class FixBasedTariff : public Tariff {
    double basecost; /* HUF */ 
    double secondcost; /* HUF/s */
    double smscost; /* HUF/sms */
    int freeseconds; /* in seconds */
  public:
    FixBasedTariff(double basecost, double minutecost_free, double minutecost, double smscost);
    virtual double calculateBill(const MonthlyPhoneLog&) const override;
};


#endif
