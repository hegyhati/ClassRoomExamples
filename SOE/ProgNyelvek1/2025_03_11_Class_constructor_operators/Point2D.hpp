#include <ostream>

class Point2D{
        double x, y;

    public: 
        Point2D(double x = 0, double y = 0);
        Point2D(const Point2D& other);

        double getX() const;
        double getY() const;

        Point2D& operator= (const Point2D& other);
        Point2D operator+(const Point2D& other) const;
        Point2D operator*(double constant) const;
        Point2D& operator*=(double constant);
};

Point2D operator*(double constant, const Point2D& point);


std::ostream& operator<<(std::ostream& s, const Point2D& P);