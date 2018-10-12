#ifndef SIMPLEVIEW_HPP
#define SIMPLEVIEW_HPP

#include "View.hpp"

class SimpleView : public View{
  
  protected:

    virtual void printPosts(list<Post> posts) const;

  public:

    SimpleView(PostManager& post_model);
};



#endif
