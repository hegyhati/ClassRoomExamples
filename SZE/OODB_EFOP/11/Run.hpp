#ifndef RUN_HPP
#define RUN_HPP

#include "Persistable.hpp"
#include "DateTime.hpp"

class Run : public Persistable
{    
  protected:
    Date date;
    std::string name;
    const std::string type;
  public:
    Run(std::string type):type(type) {}
    ~Run();
    virtual double getDistance() const =0;
    virtual Time getDuration() const =0;

    Date getDate() const;
    std::string getName() const;
    std::string getType() const;
};

#endif // RUN_HPP



