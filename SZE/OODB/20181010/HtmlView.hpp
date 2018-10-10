#ifndef HTMLVIEW_HPP
#define HTMLVIEW_HPP

#include "PostManager.hpp"

class HtmlView{
  
    PostManager& post_model;
    mutable ofstream file;

  public:

    HtmlView(PostManager& post_model, string filename);
    ~HtmlView();
    void printAll() const;
    void printBy(string author) const;
};



#endif
