#ifndef BRAKE_DISTANCE_CALC_H
#define BRAKE_DISTANCE_CALC_H

/**
 * 
 * 
 * d = v^2/(2*mu*g)
 * 
 * More information on the topic here:
 * https://en.wikipedia.org/wiki/Braking_distance
 * 
 * */

namespace szechenyi_programming
{

constexpr double ACC_GRAVITY = 9.81;

constexpr double COEFFICIENT_FRICTION = 0.6;

struct Vehicle
{
    const double friction_coeff;
    const double mass;
    // Dynamic parameters
    double velocity;
    double acceleration;
};

/**
 * Calculate instantaneous braking distance of a vehicle
 * */
double calcBrakeDistance(const Vehicle& vehicle);

/**
 * Accelerate vehicle
 * */
void accelerateVehicle(Vehicle& vehicle, const double acc, const double t);

double calcDistance(const Vehicle& vehicle, const double t);

}

#endif