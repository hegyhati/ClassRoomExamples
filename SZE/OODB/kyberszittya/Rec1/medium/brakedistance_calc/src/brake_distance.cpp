#include "BrakeDistanceCalc.h"

double szechenyi_programming::calcBrakeDistance(const Vehicle& vehicle)
{
    return (vehicle.velocity*vehicle.velocity)/(2*vehicle.friction_coeff*szechenyi_programming::ACC_GRAVITY);
}

void szechenyi_programming::accelerateVehicle(Vehicle& vehicle, const double acc, const double t)
{
    vehicle.velocity += acc * t;
}

double szechenyi_programming::calcDistance(const Vehicle& vehicle, const double t)
{
    return vehicle.velocity * t + vehicle.acceleration/2.0 * t * t;
}