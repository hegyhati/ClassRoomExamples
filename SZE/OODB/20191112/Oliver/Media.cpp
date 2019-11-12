#include "Media.h"

std::string Media::lengthStr() const
{
    int sec = length % 60;
    return std::to_string(length / 60) + ':' + (sec < 10 ? "0" : "") + std::to_string(sec);
}

std::ostream& operator<<(std::ostream& out, const Media& m)
{
    return out << m.toString();
}
