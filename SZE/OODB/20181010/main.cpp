#include "PostManager.hpp"
#include "View.hpp"

int main(){
  PostManager posts_model("Posts.txt");
  View simpleview(posts_model);
  simpleview.printAll();
  simpleview.printBy("T-800");
  
}
