#ifndef POSTDATABASE_HPP
#define POSTDATABASE_HPP

#include "Post.hpp"
#include <fstream>
#include <string>
using namespace std;


#define SIZE 1024
class PostDatabase{
  private: 
    Post items[SIZE];
    int count;
  public:
    // I/O functions
    void readFrom(istream& file);
    void writeTo(ostream& s) const;

    // Manipulations
    void orderByLikes();
    void removePostsBy(string bannedauthor="Jani");

};






#endif
