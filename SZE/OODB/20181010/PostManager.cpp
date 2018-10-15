#include "PostManager.hpp"
#include <fstream>
#include <iostream>



PostManager::PostManager(string filename) : nextid (0){
  ifstream postfile(filename);
  while(! postfile.eof()){
    try{      
      posts.push_back(Post(postfile));
      if(posts.last().getId()>=nextid) nextid = posts.last().getId()+1;
    } catch (string e) {
      cerr << "Sorry, reading post was unsuccessful...\n";
      cerr << "Error message: "<<e<<endl;
    }
  }
}

const list<Post> PostManager::getAllPosts() const {
  return posts;
}


const list<Post> PostManager::getPostsBy(string author) const {
  list<Post> toReturn;
  for(auto it=posts.cbegin(); it!= posts.cend(); ++it)
    if(it->getAuthor()==author)
      toReturn.push_back(*it);
  return toReturn;
}



