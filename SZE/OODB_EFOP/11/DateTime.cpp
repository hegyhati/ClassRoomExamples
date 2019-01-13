#include "DateTime.hpp"

std::ostream& operator << (std::ostream& s, const Date& d) {
  s << d.year << "." << d.month << "." << d.day;
  return s;
}

std::ostream& operator << (std::ostream& s, const Time& t) {
  if (t.hours() > 0) s <<" "<< t.hours() << " h";
  if (t.minutes() > 0) s <<" "<< t.minutes() << " min";
  if (t.seconds() > 0) s <<" "<< t.seconds() << " s";
  if (t.seconds() == 0 && t.minutes() == 0 && t.hours()==0) s << " 0 s";
  return s;
}

void Time::persist(std::ostream &s) const
{
  s << duration;
}

void Time::loadfrom(std::istream &s)
{
  s >> duration;
}

int Date::getYear() const
{
  return year;
}

unsigned int Date::getMonth() const
{
  return month;
}

unsigned int Date::getDay() const
{
  return day;
}

void Date::persist(std::ostream &s) const
{
  s << " " << year << " " << month << " "<< day << " ";
}

void Date::loadfrom(std::istream &s)
{
  s >> year;
  s >> month;
  s >> day;
}
