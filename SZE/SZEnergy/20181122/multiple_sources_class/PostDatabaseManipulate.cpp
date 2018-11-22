#include "PostDatabase.hpp"


void PostDatabase::orderByLikes(){
  for(int i=0;i<count-1;++i){
    for(int p=0;p<count-i-1;++p){
      if(items[p].getLikeCount() < items[p+1].getLikeCount()){
        Post temp;
        temp=items[p+1];
        items[p+1]=items[p];
        items[p]=temp;
      }
    }
  }
}


void PostDatabase::removePostsBy(string bannedauthor){
  for(int p=count-1;p>=0;--p) {
    if(items[p].getAuthor()==bannedauthor){
      for(int p2=p+1;p2<count;++p2){
        items[p2-1]=items[p2];
      }
      --count;
    }
  }
}
