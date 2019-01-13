#ifndef GPSRUN_HPP
#define GPSRUN_HPP

#include "Run.hpp"
#include "GPSMeasurementList.hpp"
#include "DateTime.hpp"

class GPSRun : public Run
{
  private:
    std::string gpxfilename;
    GPSMeasurementList track;

  public:
    GPSRun();

    virtual void persist(std::ostream& s) const override;
    virtual void loadfrom(std::istream& s) override;

    virtual Time getDuration() const override;
    virtual double getDistance() const override;

    friend std::ostream& operator << (std::ostream& s, const GPSRun& r);
};

#endif // GPSRUN_HPP
