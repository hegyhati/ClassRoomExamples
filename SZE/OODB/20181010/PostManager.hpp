#ifndef PostManager_HPP
#define PostManager_HPP

#include <list>
#include <string>
using namespace std;

#include "Post.hpp"

class PostManager{
    
    list<Post> posts;
  
  public:
  
    PostManager(string filename);
    
    void printAll() const;
    void printBy(string author) const;
  
};

#endif
