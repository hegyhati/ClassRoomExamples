#include "View.hpp"
#include <iostream>
#include <list>
using namespace std;

View::View(PostManager& post_model)
  :post_model(post_model) {}

View::~View(){}

void View::printPosts(string author) const {
  if(author=="") printPosts(post_model.getAllPosts());
  else printPosts(post_model.getPostsBy(author));
}

