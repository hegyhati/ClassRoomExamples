#include "PostManager.hpp"
#include "HtmlView.hpp"
#include "SimpleView.hpp"
#include "View.hpp"


int main(int argc, char** argv){
  PostManager posts_model("Posts.txt");

  list<View*> views;
  views.push_back(new SimpleView(posts_model));
  if(argc>1) views.push_back(new HtmlView(posts_model,argv[1]));


  
  posts_model.newPost("Grut","I am Grut.");
  
  for(auto& pview : views) {
    pview->printPosts();
    pview->printPosts("Grut");
    delete pview;
  }
  
}
