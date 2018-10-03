#ifndef POSTLIST_HPP
#define POSTLIST_HPP

#include "Post.hpp"
#include <string>
using namespace std;

#include "List.hpp"

class PostList{
    
    List<Post> posts;
  
  public:
  
    PostList(string filename);
    
    void printAll() const;
    void printBy(string author) const;
  
};

#endif
