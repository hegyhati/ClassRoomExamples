#ifndef VIEW_HPP
#define VIEW_HPP

#include "PostManager.hpp"
#include "Post.hpp"

#include <list>
using namespace std;



class View{
  
    PostManager& post_model;

  protected:

    virtual void printPosts(list<Post> posts) const = 0;

  public:

    View(PostManager& post_model);
    virtual ~View();
    void printPosts(string author="") const;
};



#endif
