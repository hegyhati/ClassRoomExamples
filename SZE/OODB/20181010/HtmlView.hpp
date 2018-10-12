#ifndef HTMLVIEW_HPP
#define HTMLVIEW_HPP

#include "View.hpp"
#include <string>

class HtmlView : public View{
  
    mutable ofstream file;
    
  protected:

    virtual void printPosts(list<Post> posts) const;
    
  public:

    HtmlView(PostManager& post_model, string filename);
    ~HtmlView();
};



#endif
