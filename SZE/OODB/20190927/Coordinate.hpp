#ifndef COORDINATE_HPP
#define COORDINATE_HPP

// Petra
class Coordinate{
    double x;
    double y;
  public:
    Coordinate(const double x, const double y);
    double getX() const;
    double getY() const;
};

// Dori
void testCoordinate();

#endif
