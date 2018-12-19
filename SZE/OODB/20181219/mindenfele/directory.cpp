#include "directory.h"

Directory::Directory(std::string name, Directory *parent) : name(name), parent(parent)
{

}

Directory::~Directory()
{
    for(auto d:subdirectories) delete d.second;
    for(auto f:files) delete f.second;
}

int Directory::mkdir(std::string dirname)
{
    if (dirname.back()=='/') dirname.pop_back();
    auto slashposition=dirname.find_last_of('/');
    if(slashposition==std::string::npos)
    {
        if(subdirectories.count(dirname)!=0) return ERROR_DIRECTORY_ALREADY_EXISTS;
        else
        {
            subdirectories[dirname]=new Directory(dirname,this);
            return 0;
        }
    }
    else
    {
        Directory* targetdir=cd(dirname.substr(0,slashposition));
        if (targetdir==nullptr) return ERROR_NO_SUCH_DIRECTORY;
        else return targetdir->mkdir(dirname.substr(slashposition+1));
    }
}

Directory *Directory::cd(std::string dirname)
{
    if (dirname=="") return this;
    auto slashposition=dirname.find_first_of('/');
    if(slashposition==std::string::npos)
    {
        if(dirname==".") return this;
        else if (dirname=="..") return parent;
        else if(subdirectories.count(dirname)!=0) return subdirectories[dirname];
        else return nullptr;
    }
    else
    {
        std::string subdirname=dirname.substr(0,slashposition);
        if (subdirname==".") return cd(dirname.substr(slashposition+1));
        else if (subdirname=="..")
        {
            if (parent==nullptr) return nullptr;
            else return parent->cd(dirname.substr(slashposition+1));
        }
        else if (subdirectories.count(subdirname)!=0)
        {
            return subdirectories[subdirname]->cd(dirname.substr(slashposition+1));
        }
        else
        {
            return nullptr;
        }
    }

}

int Directory::touch(std::string filename, std::string content)
{
    auto lastslash=filename.find_last_of("/");
    if(lastslash==std::string::npos)
    {
        if(files.count(filename)!=0) return ERROR_FILE_ALREADY_EXISTS;
        else
        {
            files[filename]=new File(filename,content);
            return 0;
        }
    }
    else
    {
        Directory* targetdir=cd(filename.substr(0,lastslash));
        if(targetdir==nullptr) return ERROR_NO_SUCH_DIRECTORY;
        else return targetdir->touch(filename.substr(lastslash+1),content);

    }
}

int Directory::cat(std::string filename, std::ostream &s)
{
    auto lastslash=filename.find_last_of("/");
    if(lastslash==std::string::npos)
    {
        if(files.count(filename)!=0)
        {
            files[filename]->cat(s);
            return 0;
        }
        else return ERROR_NO_SUCH_FILE;
    }
    else
    {
        Directory* targetdir=cd(filename.substr(0,lastslash));
        if(targetdir==nullptr) return ERROR_NO_SUCH_DIRECTORY;
        else return targetdir->cat(filename.substr(lastslash+1),s);

    }
}

void Directory::ls(std::ostream &s) const
{
    for(const auto& d:subdirectories) s<<d.first<<"/"<<std::endl;
    for(const auto& f:files) s<<f.first<<std::endl;
}

void Directory::lstree(std::ostream &s) const
{
    s<<pwd()<<std::endl;
    lstreedepth(s,"");
}

std::string Directory::pwd() const
{
    if(parent!=nullptr) return parent->pwd()+name+"/";
    else return name+"/";
}

void Directory::lstreedepth(std::ostream &s, std::string indent) const
{
    for(auto d: subdirectories)
    {
        bool last=(d.first==subdirectories.rbegin()->first) && files.empty();
        s<<indent<<(last?"└─":"├─")<<d.first<<"/"<<std::endl;
        d.second->lstreedepth(s,indent+(last?"  ":"│ "));
    }
    for(auto f: files)
    {
        bool last=(f.first==files.rbegin()->first);
        s<<indent<<(last?"└─":"├─")<<f.first<<std::endl;
    }
}
