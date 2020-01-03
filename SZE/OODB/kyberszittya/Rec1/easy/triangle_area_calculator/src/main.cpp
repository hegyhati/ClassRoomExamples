
#include <iostream>

#include "triangle.h"


int main(int argc, char** argv)
{
    double a,b,c;
    std::cout << "Give me some traingle parameters" << '\n';
    std::cout << "Side a [cm]: ";
    std::cin  >> a;
    std::cout << "Side b [cm]: ";
    std::cin  >> b;
    std::cout << "Side c [cm]: ";
    std::cin  >> c;
    Triangle triangle({a,b,c});
    if (validTriangle(triangle))
    {
        std::cout << "Area [cm^2]: " << calcTriangleArea(triangle) << '\n';
    }
    else
    {
        std::cerr << "Invalid triangle\n";
    }
    
    return 0;
}