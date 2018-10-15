#ifndef PostManager_HPP
#define PostManager_HPP

#include <list>
#include <string>
using namespace std;

#include "Post.hpp"

class PostManager{
  
    const string filename;
    list<Post> posts;
    int nextid;
  
  public:
  
    PostManager(string filename);

    const list<Post> getAllPosts() const;
    const list<Post> getPostsBy(string author) const;
    int newPost(string author, string content);
  
};

#endif
