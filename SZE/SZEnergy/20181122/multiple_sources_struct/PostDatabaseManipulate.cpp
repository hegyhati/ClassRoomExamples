#include "PostDatabase.hpp"


void orderByLikes(PostDatabase& posts){
  for(int i=0;i<posts.count-1;++i){
    for(int p=0;p<posts.count-i-1;++p){
      if(posts.items[p].likecount < posts.items[p+1].likecount){
        Post temp;
        temp=posts.items[p+1];
        posts.items[p+1]=posts.items[p];
        posts.items[p]=temp;
      }
    }
  }
}


void removePostsBy(PostDatabase& posts, string bannedauthor){
  for(int p=posts.count-1;p>=0;--p) {
    if(posts.items[p].author==bannedauthor){
      for(int p2=p+1;p2<posts.count;++p2){
        posts.items[p2-1]=posts.items[p2];
      }
      --posts.count;
    }
  }
}
