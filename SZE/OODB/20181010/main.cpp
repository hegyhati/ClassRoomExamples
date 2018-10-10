#include "PostManager.hpp"
#include "HtmlView.hpp"
#include "View.hpp"

int main(int argc, char** argv){
  PostManager posts_model("Posts.txt");
  
  View simpleview(posts_model);
  simpleview.printAll();
  simpleview.printBy("T-800");

  if(argc>1){
    HtmlView htmlview(posts_model,argv[1]);
    htmlview.printAll();
    htmlview.printBy("T-800");
  }
  
}
