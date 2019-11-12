#ifndef VIDEO_H
#define VIDEO_H

#include <string>
#include "Media.h"

class Video : public Media
{
    const int hpx,vpx;
  public:
    Video(std::string title, int duration, int hpx, int vpx);
    virtual void print(std::ostream& = std::cout) const override;
};

#endif // VIDEO_H
