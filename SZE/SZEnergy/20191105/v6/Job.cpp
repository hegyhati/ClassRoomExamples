#include "Job.hpp"

Job::Job(std::string name, int startday, int duration)
  : name(name),startday(startday),endday(startday+duration-1) {}

bool Job::overlaps(const Job& other) const{
  return (getEndDay()>=other.getStartDay())
      && (other.getEndDay()>=getStartDay());
}
