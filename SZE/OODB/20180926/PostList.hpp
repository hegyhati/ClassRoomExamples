#ifndef POSTLIST_HPP
#define POSTLIST_HPP

#include "Post.hpp"
#include <string>
using namespace std;

class PostList{
    
    struct PLItem{
      Post data;
      struct PLItem* next;
    };

    struct PLItem* posts;
    
    void addPost(Post post);
    void popPost();
  
  public:
  
    PostList(string filename);
    ~PostList();
    
    void printAll() const;
    void printBy(string author) const;
  
};

#endif
