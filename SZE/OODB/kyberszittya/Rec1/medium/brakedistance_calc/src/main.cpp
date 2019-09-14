#include "BrakeDistanceCalc.h"

#include <iostream>

using namespace szechenyi_programming;
using namespace std;

int main(int argc, char** argv)
{    
    // Vehicle parameters
    double acc;
    double mass;
    // Simulation parameters
    double t_end;
    unsigned int steps;    
    cout << "Brake distance calculation\n"  << "----------" << '\n';
    cout << "Simulation parameters" << '\n' << "----------" << '\n';
    cout << "Simulation duration [s]: ";
    cin  >> t_end;
    cout << "Simulation steps: ";
    cin  >> steps;
    const double dt = t_end/steps;
    cout << "Granularity: " << dt;
    cout << "\nVehicle parameters" << '\n' << "----------" << '\n';
    cout << "Vehicle mass [kg]: ";    
    cin  >> mass;    
    cout << "Vehicle acceleration [m/s^2]: ";
    cin  >> acc;
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
    return 0;
}