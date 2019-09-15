#include <iostream>
#include <fstream>
#include <sstream>

#include "comp_interest.h"


using namespace std;


int main(int argc, char** argv)
{
    ifstream file("../data/interests.dat");
    if (file.is_open())
    {
        string line;
        while(getline(file, line))
        {
            stringstream ss(line);
            double cash, interest, target_cash;
            ss   >> cash;
            ss   >> interest;
            interest /= 100.0;
            ss   >> target_cash;
            cout << "Starting cash [EUR]: " << cash << '\n';
            cout << "Compound interest [%]: " << interest << '\n';
            cout << "Desired cash [EUR]: " << target_cash << '\n';
            cout << "Years to get cash: " << ceil(yearsToTargetCash(cash, interest, target_cash)) << '\n';
            cout << '\n';
        }
    }
    return 0;
}