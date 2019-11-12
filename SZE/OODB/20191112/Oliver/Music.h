#pragma once

#include "Media.h"

class Music
    : public Media
{
    const std::string artist;
public:
    Music(const std::string& artist, const std::string& title, int length)
        : Media(title, length), artist(artist)
    {}
    virtual std::string toString() const;
    virtual void print() const;
};
