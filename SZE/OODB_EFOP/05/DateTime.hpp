#ifndef DATETIME_HPP
#define DATETIME_HPP

class Date {
  public:
    const int year;
    const unsigned int month;
    const unsigned int day;

    Date(int year, unsigned int month, unsigned int day)
      :year(year),month(month),day(day) {}
};

ostream& operator << (ostream& s, const Date& d) {
  s << d.year << "." << d.month << "." << d.day;
  return s;
}


class Time{
  private:
    const int duration;
  public:
    Time(int seconds) : duration(seconds) {}
    Time(int minutes, int seconds)
      : duration(minutes*60+seconds) {}
    Time(int hours, int minutes, int seconds)
      : duration (3600* hours + 60* minutes + seconds) {}
    int getDurationInSeconds() const {return duration;}
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

ostream& operator << (ostream& s, const Time& t) {
  if (t.hours() > 0) s <<" "<< t.hours() << " h";
  if (t.minutes() > 0) s <<" "<< t.minutes() << " min";
  if (t.seconds() > 0) s <<" "<< t.seconds() << " s";
  return s;
}

#endif
