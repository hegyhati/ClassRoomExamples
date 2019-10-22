#ifndef JOB_HPP
#define JOB_HPP

#include <string>

struct Job{
  std::string name;
  int startday;
  int duration;
  bool overlaps(const Job& other) const;
};


#endif 


