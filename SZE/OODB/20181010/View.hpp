#ifndef VIEW_HPP
#define VIEW_HPP

#include "PostManager.hpp"

class View{
  
    PostManager& post_model;

  public:

    View(PostManager& post_model);
    void printAll() const;
    void printBy(string author) const;
};



#endif
