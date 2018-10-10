#include "PostManager.hpp"
#include <fstream>
#include <iostream>



PostManager::PostManager(string filename) {
  ifstream postfile(filename);
  while(! postfile.eof()){
    try{      
      posts.push_back(Post(postfile));
    } catch (string e) {
      cerr << "Sorry, reading post was unsuccessful...\n";
      cerr << "Error message: "<<e<<endl;
    }
  }
}

void PostManager::printAll() const {
  cout<<"List of posts:\n";
  for(auto it=posts.cbegin(); it!= posts.cend(); ++it)
    it->print();
}


void PostManager::printBy(string author)const {
  cout<<"Posts by "<<author<<":\n";
  for(auto it=posts.cbegin(); it!= posts.cend(); ++it)
    if(it->getAuthor()==author)
      cout<<"\t- "<<it->getContent()<<endl;
}



