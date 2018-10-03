#ifndef POST_HPP
#define POST_HPP

#include <fstream>
#include <string>
using namespace std;

class Post {
    string author;
    string content;
  public:
    Post(string author="", string content="");
    Post(ifstream& file);
    
    void print() const;
    string getAuthor() const;
    string getContent() const;
    
};






#endif
