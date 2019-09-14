#include <cmath>

struct Triangle
{
    double a,b,c;
};

inline double calcSemiperimeter(const Triangle& triangle);
bool validTriangle(const Triangle& triangle);
double calcTriangleArea(const Triangle& triangle);