#ifndef JOB_HPP
#define JOB_HPP

#include <string>

class Job{
    std::string name;
    int startday;
    int endday;
  public:
    Job(std::string name="Job", int startday=0, int duration=0);
    bool overlaps(const Job& other) const;
    std::string getName() const {return name;}
    int getStartDay() const {return startday;}
    //int getDuration() const {return endday-startday+1;}
    int getEndDay() const {return endday;}
    static bool earlier(const Job& first, const Job& second);
};


#endif 


