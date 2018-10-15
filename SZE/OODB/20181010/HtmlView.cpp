#include "HtmlView.hpp"

HtmlView::HtmlView(PostManager& post_model, string filename)
  :View(post_model), file(filename){
  file<<"<html>"<<endl
      <<"\t<body>"<<endl;
}

HtmlView::~HtmlView(){
  file<<"\t</body>"<<endl
      <<"</html>"<<endl;
  file.close();
}

void HtmlView::printPosts(list<Post> posts) const {
  file<<"\t\t<ul>"<<endl;
  for(const auto& post : posts)
    file<<"\t\t\t<li id=\""<<post.getId()<<"\">"<<post.getAuthor()<<":"<<post.getContent()<<"</li>"<<endl;
  file<<"\t\t</ul>"<<endl;
}
