#ifndef FILE_H
#define FILE_H

#include <string>
#include <iostream>

class File
{
public:
    File(std::string name, std::string content="");
    std::string getName() const;
    std::string getContent() const;
    void cat(std::ostream& s=std::cout) const;

private:
    std::string name;
    std::string content;
};


#endif // FILE_H
