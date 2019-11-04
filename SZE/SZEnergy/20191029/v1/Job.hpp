#ifndef JOB_HPP
#define JOB_HPP

#include <string>

class Job{
    std::string name;
    int startday;
    int duration;
  public:
    bool overlaps(const Job& other) const;
    std::string getName() const {return name;}
    void setName(std::string newname){name=newname;}
    int getStartDay() const {return startday;}
    void setStartDay(int newstartday){startday=newstartday;}
    int getDuration() const {return duration;}
    void setDuration(int newduration){duration=newduration;}
};


#endif 


