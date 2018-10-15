#ifndef POST_HPP
#define POST_HPP

#include <fstream>
#include <string>
using namespace std;

class Post {
    const int id;
    const string author;
    const string content;
  public:
    Post(int id, string author="", string content="");
    Post(ifstream& file);
    
    string getAuthor() const;
    string getContent() const;
    int getId() const;    
};


ostream& operator<<(ostream& file, const Post& post);






#endif
