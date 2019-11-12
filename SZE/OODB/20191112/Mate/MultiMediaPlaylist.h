#ifndef MULTIMEDIAPLAYLIST_H
#define MULTIMEDIAPLAYLIST_H

/*
- Gondoskodjon r?la, hogy k?s?bb a kapott objektumok mem?riater?lete felszabad?t?sra ker?lj?n.
- `sortByLength()`: Rendezze a lista elemeit hosszuk szerint n?vekv? sorrendbe.
- `sortByTitle()`: Rendezze a lista elemeit c?m szerint ?b?c?sorrendbe.
- `print()`: ?rja ki a lista elemeit.
*/

#include <list>
#include "Media.h"

class MultiMediaPlaylist
{
    std::list<Media*> tracks;
  public:
    MultiMediaPlaylist();
    MultiMediaPlaylist( const MultiMediaPlaylist& other);
    ~MultiMediaPlaylist();
    const Media* current() const;
    void add(Media*newtrack);
    void skip();
    void sortByLength();
    void sortByTitle();
    void print() const;
};

#endif // MULTIMEDIAPLAYLIST_H
