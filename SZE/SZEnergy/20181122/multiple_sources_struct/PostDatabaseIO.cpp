#include "PostDatabase.hpp"


void readPosts(PostDatabase& posts, istream& file){
  posts.count=0;
  while(!file.eof()) {
    if(readPost(posts.items[posts.count],file)) {
      posts.count++;
    } else {
      /* Handle bad input */
    }
  }
}

void writePosts(const PostDatabase& posts, ostream& s){
  for(int p=0; p<posts.count; ++p) {
    writePost(posts.items[p],s);
  }
}


