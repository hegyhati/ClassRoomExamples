#ifndef DATETIME_HPP
#define DATETIME_HPP

#include <iostream>

class Date {
  public:
    const int year;
    const unsigned int month;
    const unsigned int day;

    Date(int year, unsigned int month, unsigned int day)
      :year(year),month(month),day(day) {}
};

std::ostream& operator << (std::ostream& s, const Date& d);


class Time{
  private:
    int duration;
  public:
    Time(int seconds=0) : duration(seconds) {}
    Time(int minutes, int seconds)
      : duration(minutes*60+seconds) {}
    Time(int hours, int minutes, int seconds)
      : duration (3600* hours + 60* minutes + seconds) {}

    void persist(std::ostream& s) const;
    void loadfrom(std::istream& s);

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
