#include <cmath>

const inline double yearsToTargetCash(const double& cash, const double& interest, const double& target_cash)
{
    return std::log(target_cash/cash)/std::log(1.0+interest);
}