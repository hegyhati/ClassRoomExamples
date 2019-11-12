#ifndef MEDIA_H
#define MEDIA_H

#include <string>
#include <iostream>

class Media
{
  protected:
    const std::string title;
    const int duration;
  public:
    Media(std::string title, int duration);
    virtual ~Media();
    virtual void print(std::ostream& = std::cout) const =0;
    static bool compareByTitle(const Media* first, const Media* second);    
    static bool compareByDuration(const Media* first, const Media* second);
};

std::ostream& operator << (std::ostream& s, const Media& media);

#endif // MEDIA_H
