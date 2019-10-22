#include "Job.hpp"

bool Job::overlaps(const Job& other) const{
  return (startday+duration-1>=other.startday) && (other.startday+other.duration-1>=startday);
}
