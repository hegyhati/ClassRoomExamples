#include "triangle.h"


inline double calcSemiperimeter(const Triangle& triangle)
{
    return (triangle.a+triangle.b+triangle.c)/2.0;
}

/**
 * Check if triangle is correct using triangle equations
 * */
bool validTriangle(const Triangle& triangle)
{
    if (std::abs(triangle.a - triangle.b) < triangle.c && triangle.c < triangle.a + triangle.b)
    {
        return true;
    }
    else
    {
        return false;
    }
    
}

/**
 * Use Heron's formula. It's cool.
 * A = sqrt()
 * */
double calcTriangleArea(const Triangle& triangle)
{
    double s = calcSemiperimeter(triangle);
    return std::sqrt(s*(s-triangle.a)*(s-triangle.b)*(s-triangle.c));
}
