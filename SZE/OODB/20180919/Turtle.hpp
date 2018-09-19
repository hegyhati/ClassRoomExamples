#ifndef TURTLE_HPP
#define TURTLE_HPP

#include <iostream>
#include <fstream>

class Turtle {
    double x;
    double y;
    double alpha;
    std::ofstream image;

    double rad(double degree);
    double svgX();
    double svgY();
  public:
    Turtle();

    void fd(double distance);
    void lt(double degrees);
    void rt(double degrees);

    double getX() const;
    double getY() const;
    double getAlpha() const;

    void interpreter(char* filename);
};





#endif
