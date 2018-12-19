#ifndef DIRECTORY_H
#define DIRECTORY_H

#include "file.h"
#include <string>
#include <iostream>
#include <map>

class Directory
{
public:
    Directory(std::string name,Directory *parent=nullptr);
    ~Directory();
    std::string pwd() const;
    void ls(std::ostream& s=std::cout) const;
    void lstree(std::ostream& s=std::cout) const;
    int mkdir(std::string dirname);
    Directory* cd(std::string dirname);
    int touch(std::string filename, std::string content="");
    int cat(std::string filename, std::ostream& s=std::cout);


    static const int ERROR_NO_SUCH_DIRECTORY=1;
    static const int ERROR_NO_SUCH_FILE=2;
    static const int ERROR_DIRECTORY_ALREADY_EXISTS=3;
    static const int ERROR_FILE_ALREADY_EXISTS=4;
private:
    std::string name;
    Directory *parent;
    std::map<std::string,Directory*> subdirectories;
    std::map<std::string,File*> files;

    void lstreedepth(std::ostream& s, std::string indent="") const ;

};

#endif // DIRECTORY_H
