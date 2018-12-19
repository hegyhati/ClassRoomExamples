#include "file.h"

File::File(std::string name, std::string content) : name(name),content(content)
{}

std::string File::getName() const
{
    return name;
}

std::string File::getContent() const
{
    return content;
}

void File::cat(std::ostream &s) const
{
    s<<content<<std::endl;
}


