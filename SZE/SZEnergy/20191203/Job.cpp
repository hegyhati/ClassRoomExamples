#include "Job.hpp"

Job::Job(std::string name, int startday, int duration)
  : name(name),startday(startday),endday(startday+duration-1) {}

bool Job::overlaps(const Job& other) const{
  return (getEndDay()>=other.getStartDay())
      && (other.getEndDay()>=getStartDay());
}

bool Job::earlier(const Job& first, const Job& second) {
  return first.getStartDay() < second.getStartDay();
}

