#include "SimpleView.hpp"
#include <iostream>

SimpleView::SimpleView(PostManager& post_model)
  :View(post_model) {}

void SimpleView::printPosts(list<Post> posts) const {  
  cout<<endl;
  for(const auto& post : posts)
    cout<<post.getAuthor()<<":"<<post.getContent()<<endl;
  cout<<endl;
}
