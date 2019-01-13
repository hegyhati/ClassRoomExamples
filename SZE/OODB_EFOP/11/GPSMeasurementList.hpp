#ifndef GPSMEASUREMENTLIST_HPP
#define GPSMEASUREMENTLIST_HPP

#include "GPSMeasurement.hpp"
#include <iostream>
#include <string>

class GPSMeasurementList{

  private:

    struct GPSMeasurementListElement{
      GPSMeasurement data;
      GPSMeasurementListElement *next;
    };

    GPSMeasurementListElement* head=nullptr;

  public:
    ~GPSMeasurementList();

    void add(GPSMeasurement GPSMeasurement);
    int size() const;
    GPSMeasurement operator [] (int idx) const ;
};

#endif // GPSMEASUREMENTLIST_HPP
