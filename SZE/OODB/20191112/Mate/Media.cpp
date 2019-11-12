#include "Media.h"

Media::Media(std::string title, int duration)
  :title(title),duration(duration)
{
  
}

Media::~Media()
{
  
}

bool Media::compareByTitle(const Media *first, const Media *second)
{
  return first->title < second->title;
}

bool Media::compareByDuration(const Media *first, const Media *second)
{  
  return first->duration < second->duration;
}

std::ostream &operator <<(std::ostream &s, const Media &media)
{
  media.print(s);
  return s;
}
