#ifndef RUN_HPP
#define RUN_HPP

#include <string>


class Run {
  public:
    double distance;
    double duration;
    std::string name;

    void input();
    void print() const;
};

#endif
