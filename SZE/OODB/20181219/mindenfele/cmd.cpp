#include "cmd.h"
#include <sstream>

void cmd::run()
{
    std::string fullcommand;
    std::string command;
    std::string argument1;
    std::string argument2;
    Directory* targetdir;

    do
    {
        printPrompt();
        std::getline(std::cin,fullcommand);
        std::istringstream line(fullcommand);
        command=argument1=argument2="";
        line>>command;
        line>>argument1;
        line>>argument2;

        if(command=="help")
        {
            std::cout << "Available commands: "
                      << "help,exit,ls,lstree,cd,mkdir,touch,cat"
                      << std::endl;
        }
        else if (command=="exit") {}
        else if (command=="ls")
        {
            if(argument1=="") current->ls();
            else if((targetdir=trycd(argument1))!=nullptr) targetdir->ls();
        }
        else if (command=="lstree")
        {
            if(argument1=="") current->lstree();
            else if((targetdir=trycd(argument1))!=nullptr) targetdir->lstree();
        }
        else if (command=="cd")
        {
            if(argument1=="") std::cout<<"No directory is given"<<std::endl;
            else if((targetdir=trycd(argument1))!=nullptr) current=targetdir;
        }
        else if (command=="mkdir")
        {
            if(argument1=="")
                std::cout<<"No directory name given"<<std::endl;
            else
            {
                switch(current->mkdir(argument1))
                {
                case Directory::ERROR_DIRECTORY_ALREADY_EXISTS:
                    std::cout<<"Directory already exists"<<std::endl;
                    break;
                case Directory::ERROR_NO_SUCH_DIRECTORY:
                    std::cout<<"One of the directories in the path do not exist"<<std::endl;
                    break;
                }
            }
        }
        else if (command=="touch")
        {
            if(argument1=="")
                std::cout<<"No file name given"<<std::endl;
            else
            {
                switch(current->touch(argument1,argument2))
                {
                case Directory::ERROR_FILE_ALREADY_EXISTS:
                    std::cout<<"File already exists"<<std::endl;
                    break;
                case Directory::ERROR_NO_SUCH_DIRECTORY:
                    std::cout<<"One of the directories in the path do not exist."<<std::endl;
                    break;
                }
            }
        }
        else if (command=="cat")
        {
            if(argument1=="")
                std::cout<<"No directory name given"<<std::endl;
            else
            {
                switch(current->cat(argument1))
                {
                case Directory::ERROR_NO_SUCH_FILE:
                    std::cout<<"The file does not exist."<<std::endl;
                    break;
                case Directory::ERROR_NO_SUCH_DIRECTORY:
                    std::cout<<"One of the directories in the path do not exist."<<std::endl;
                    break;
                }
            }
        }
        else std::cout<<"Unknown command"<<std::endl;
    } while (command!="exit");
    std::cout<<"Bye-bye"<<std::endl;
}

cmd::~cmd()
{
    delete root;
}

void cmd::printPrompt() const
{
    std::cout<<current->pwd()<<"$ ";
}

Directory *cmd::trycd(std::string dirname) const
{
    Directory* targetdir;
    if(dirname[0]=='/') targetdir=root->cd(dirname.substr(1));
    else targetdir=current->cd(dirname);
    if(targetdir==nullptr)
    {
        std::cout<<"One of the directories in the path do not exist."<<std::endl;
        return nullptr;
    }
    else return targetdir;
}
