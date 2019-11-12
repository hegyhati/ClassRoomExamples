#include "Music.h"
#include <iostream>

Music::Music(std::string artist, std::string title, int duration)
  :Media(title,duration),artist(artist)
{
  
}

void Music::print(std::ostream & s) const
{
  s<<artist<<" - "<<title<<" ("<<duration/60<<":"<<duration%60<<")";
}
