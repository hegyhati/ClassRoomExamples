#include <iostream>
#include <fstream>
#include <sstream>

#include "triangle.h"

int main(int argc, char** argv)
{
    std::ifstream triangle_input_file(argv[1]);
    if (triangle_input_file.is_open())
    {
        std::string line;
        while(getline(triangle_input_file, line))
        {
            std::stringstream ss(line);
            double a,b,c;
            ss        >> a;
            ss        >> b;
            ss        >> c;
            std::cout << "Sides [cm]: " << a << '\t' << b << '\t' << c << '\n';
            Triangle triangle({a,b,c});
            if (validTriangle(triangle))
            {
                std::cout << "Area [cm^2]: " << calcTriangleArea(triangle) << '\n';
            }
            else
            {
                std::cerr << "Invalid triangle\n";
            }
        }
    }
    
    
    return 0;
}