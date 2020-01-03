#include "BrakeDistanceCalc.h"

#include <fstream>
#include <sstream>
#include <string>
#include <iostream>

using namespace szechenyi_programming;
using namespace std;

int main(int argc, char** argv)
{
    ifstream vehicle_files(argv[1]);
    if (vehicle_files.is_open())
    {
        string line;
        while(getline(vehicle_files, line))
        {
            // Vehicle parameters
            double acc;
            double mass;
            // Simulation parameters
            double t_end;
            unsigned int steps;
            stringstream ss(line);
            ss   >> t_end;
            ss   >> steps;
            const double dt = t_end/steps;
            ss   >> mass;            
            ss   >> acc;
            cout << "Read vehicle from file" << '\n';
            cout << "Brake distance calculation\n"  << "----------" << '\n';
            cout << "Simulation parameters" << '\n' << "----------" << '\n';
            cout << "Simulation duration [s]: " << t_end << '\n';
            cout << "Simulation steps: " << steps << '\n';
            cout << "Granularity: " << dt << '\n';
            cout << "\nVehicle parameters" << '\n' << "----------" << '\n';
            cout << "Vehicle mass [kg]: " << mass << '\n';    
            cout << "Vehicle acceleration [m/s^2]: " << acc << '\n';
            // Start our simulation
            double t = 0.0;
            double s = 0.0;
            Vehicle vehicle({COEFFICIENT_FRICTION, mass, 0.0, 0.0});    
            // Run our simulation
            for (int i = 0.0; i < steps; i++)
            {
                accelerateVehicle(vehicle, acc, dt);
                t += dt;
                s += calcDistance(vehicle, dt);
                cout << "Vehicle speed at time [" << t << " secs]: " << vehicle.velocity << " [m/s]" << '\n';
                cout << "Distance so far [m]: " << calcDistance(vehicle, t) << '\n';
                cout << "Braking distance [m]: " << calcBrakeDistance(vehicle) << '\n';
            }
            cout << '\n';
        }
    }
    return 0;
    
}