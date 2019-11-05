#include "FixBasedTariff.hpp"

FixBasedTariff::FixBasedTariff(double basecost, double minutecost_free, double minutecost, double smscost)
  : basecost(basecost), secondcost(minutecost/60), smscost(smscost), freeseconds(60*basecost/minutecost_free) {}


double FixBasedTariff::calculateBill(const MonthlyPhoneLog& mpl) const {
  double totalCost = basecost;
  totalCost += mpl.smscount * smscost;
  if (mpl.seconds > freeseconds)
    totalCost += (mpl.seconds - freeseconds) * secondcost;
  return totalCost;
}
