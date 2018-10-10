#include "PostManager.hpp"
#include "HtmlView.hpp"

int main(){
  PostManager posts_model("Posts.txt");
  HtmlView simpleview(posts_model,"index.html");
  simpleview.printAll();
  simpleview.printBy("T-800");
  
}
