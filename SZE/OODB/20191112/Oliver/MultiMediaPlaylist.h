#pragma once

#include <deque>

#include "Media.h"

class MultiMediaPlaylist
{
    std::deque<Media*> playlist;
public:
    MultiMediaPlaylist() = default;
    MultiMediaPlaylist(const MultiMediaPlaylist& other);
    ~MultiMediaPlaylist();
    const Media* current() const;
    void add(Media*);
    void skip();
    void sortByLength();
    void sortByTitle();
    void print() const;
};

