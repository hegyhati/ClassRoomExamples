#include "PostManager.hpp"

int main(){
  PostManager postlist("Posts.txt");
  postlist.printAll();
  postlist.printBy("T-800");
}
