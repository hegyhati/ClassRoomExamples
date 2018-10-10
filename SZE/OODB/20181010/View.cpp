#include "View.hpp"
#include <iostream>
#include <list>
using namespace std;

View::View(PostManager& post_model)
  :post_model(post_model) {}

void View::printAll() const {
  list<Post> allposts = post_model.getAllPosts();
  cout<<"List of posts:\n";
  for(auto it=allposts.cbegin(); it!= allposts.cend(); ++it)
    cout<<it->getAuthor()<<":"<<it->getContent()<<endl<<endl;
}

void View::printBy(string author) const {
  list<Post> posts = post_model.getPostsBy(author);
  cout<<"Posts by "<<author<<":\n";
  for(auto it=posts.cbegin(); it!= posts.cend(); ++it)
      cout<<"\t- "<<it->getContent()<<endl;
}

