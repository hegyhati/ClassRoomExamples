#include "SimpleTariff.hpp"


SimpleTariff::SimpleTariff(double minutecost, double smscost, int base) : secondcost(minutecost/60), smscost(smscost), base(base) {}

double SimpleTariff::calculateBill(const MonthlyPhoneLog& mpl) const {
  double totalCost = 0;
  totalCost += mpl.smscount * smscost;
  int paidseconds = base * (mpl.seconds / base + ((mpl.seconds % base)?1:0) ); 
  totalCost += paidseconds * secondcost;
  return totalCost;
}
