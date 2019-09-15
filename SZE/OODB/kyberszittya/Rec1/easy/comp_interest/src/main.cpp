#include <iostream>

#include "comp_interest.h"

using namespace std;

int main(int argc, char** argv)
{
    double cash, interest, target_cash;
    cout << "Starting cash [EUR]: ";
    cin  >> cash;
    cout << "Compound interest [%]: ";
    cin  >> interest;
    interest /= 100.0;
    cout << "Desired cash [EUR]: ";
    cin  >> target_cash;
    cout << "Years to get cash: " << ceil(yearsToTargetCash(cash, interest, target_cash)) << '\n';

    return 0;
}