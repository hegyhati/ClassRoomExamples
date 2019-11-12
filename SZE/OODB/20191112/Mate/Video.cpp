#include "Video.h"
#include <iostream>

Video::Video(std::string title, int duration, int hpx, int vpx)
  :Media (title,duration), hpx(hpx), vpx(vpx)
{
  
}

void Video::print(std::ostream & s) const
{
    s<<title<<" ("<<duration/60<<":"<<duration%60<<" - "<<hpx<<" x "<<vpx<<")";
}
