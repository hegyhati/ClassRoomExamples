#pragma once

#include "Media.h"

class Video
    : public Media
{
    const int width, height;
public:
    Video(const std::string& title, int length, int width, int height)
        : Media(title, length), width(width), height(height)
    {}
    virtual std::string toString() const;
    virtual void print() const;
};
