#ifndef DATETIME_HPP
#define DATETIME_HPP

#include <iostream>
#include "Persistable.hpp"

class Date : public Persistable {

  private:

    int year;
    unsigned int month;
    unsigned int day;

  public:

    Date(int year=0, unsigned int month=0, unsigned int day=0)
      :year(year),month(month),day(day) {}

    virtual void persist(std::ostream& s) const override;
    virtual void loadfrom(std::istream& s) override;
    int getYear() const;
    unsigned int getMonth() const;
    unsigned int getDay() const;

    friend std::ostream& operator << (std::ostream& s, const Date& d);
};




class Time : public Persistable {
  private:
    int duration;
  public:
    Time(int seconds=0) : duration(seconds) {}
    Time(int minutes, int seconds)
      : duration(minutes*60+seconds) {}
    Time(int hours, int minutes, int seconds)
      : duration (3600* hours + 60* minutes + seconds) {}

    virtual void persist(std::ostream& s) const override;
    virtual void loadfrom(std::istream& s) override;

    int getDuration() const {return duration;}
    void setDuration(int duration) {this->duration=duration;}

    int hours() const { return duration / 3600; }
    int minutes() const { return (duration % 3600) / 60; }
    int seconds() const { return duration % 60; }

    bool operator > (const Time& other) {
      return duration > other.duration;
    }
    bool operator < (const Time& other) {
      return duration < other.duration;
    }
    bool operator == (const Time& other) {
      return duration == other.duration;
    }
    Time operator - (const Time& other){
      return Time(duration-other.duration);
    }    
};

std::ostream& operator << (std::ostream& s, const Time& t);

#endif
