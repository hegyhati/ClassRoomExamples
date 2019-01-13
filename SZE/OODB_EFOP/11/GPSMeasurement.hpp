#ifndef GPSMEASUREMENT_HPP
#define GPSMEASUREMENT_HPP

#include "Persistable.hpp"
#include "DateTime.hpp"

class GPSMeasurement : public Persistable
{
  private:
    Time time;
    double x=0;
    double y=0;
  public:
    virtual void persist(std::ostream& s) const override;
    virtual void loadfrom(std::istream& s) override;

    double getY() const;
    double getX() const;
    Time getTime() const;
};

#endif // GPSMEASUREMENT_HPP
