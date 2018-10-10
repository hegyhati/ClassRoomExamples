#ifndef POSTLIST_HPP
#define POSTLIST_HPP

#include <list>
#include <string>
using namespace std;

#include "Post.hpp"

class PostList{
    
    list<Post> posts;
  
  public:
  
    PostList(string filename);
    
    void printAll() const;
    void printBy(string author) const;
  
};

#endif
