#ifndef MUSIC_H
#define MUSIC_H

#include <string>
#include "Media.h"

class Music : public Media
{
    const std::string artist;
  public:
    Music(std::string artist, std::string title, int duration);
    virtual void print(std::ostream& = std::cout) const override;
};

#endif // MUSIC_H
