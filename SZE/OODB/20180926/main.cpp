#include "PostList.hpp"

int main(){
  PostList postlist("Posts.txt");
  postlist.printAll();
  postlist.printBy("T-800");
}
