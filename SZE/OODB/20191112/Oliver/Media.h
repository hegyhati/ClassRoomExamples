#pragma once

#include <string>

class Media {
protected:
    const std::string title;
    const int length;
    
    std::string lengthStr() const;
public:
    Media(const std::string& title, int length)
        : title(title), length(length)
    {}
    virtual std::string toString() const = 0;
    virtual void print() const = 0;
    int getLength() const { return length; }
    const std::string& getTitle() const { return title; }
};

#include <iostream>

std::ostream& operator<<(std::ostream&, const Media&);
