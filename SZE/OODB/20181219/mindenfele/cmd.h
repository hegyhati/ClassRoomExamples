#ifndef CMD_H
#define CMD_H

#include <iostream>
#include <string>
#include "directory.h"
#include "file.h"

class cmd
{
public:
    void run();
   ~cmd();
private:
   Directory* const root=new Directory("");
   Directory* current=root;
   void printPrompt() const;
   Directory * trycd(std::string dirname) const;
};

#endif // CMD_H
