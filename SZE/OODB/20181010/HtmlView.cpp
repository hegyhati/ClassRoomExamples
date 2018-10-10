#include "HtmlView.hpp"
#include <iostream>
#include <list>
using namespace std;

HtmlView::HtmlView(PostManager& post_model, string filename)
  :post_model(post_model), file(filename){
  file<<"<html>"<<endl
      <<"  <body>"<<endl;
}

HtmlView::~HtmlView(){
  file<<"  </body>"<<endl
      <<"</html>"<<endl;
  file.close();
}

void HtmlView::printAll() const {
  list<Post> allposts = post_model.getAllPosts();
  file<<"    <h1>List of posts</h1>";
  file<<"    <ul>"<<endl;
  for(auto it=allposts.cbegin(); it!= allposts.cend(); ++it)
    file<<"      <li>"<<it->getAuthor()<<":"<<it->getContent()<<"</li>"<<endl;
  file<<"    </ul>"<<endl;
}

void HtmlView::printBy(string author) const {
  list<Post> posts = post_model.getPostsBy(author);
  file<<"    <h1>List of posts by "<<author<<"</h1>";
  file<<"    <ul>"<<endl;
  for(auto it=posts.cbegin(); it!= posts.cend(); ++it)
    file<<"      <li>"<<it->getContent()<<"</li>"<<endl;
  file<<"    </ul>"<<endl;
}

