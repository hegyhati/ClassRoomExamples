#include "PostList.hpp"
#include <fstream>
#include <iostream>



PostList::PostList(string filename) {
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

void PostList::printAll() const {
  cout<<"List of posts:\n";
  for(list<Post>::const_iterator it=posts.cbegin(); it!= posts.cend(); ++it)
    it->print();
}


void PostList::printBy(string author)const {
  cout<<"Posts by "<<author<<":\n";
  for(list<Post>::const_iterator it=posts.cbegin(); it!= posts.cend(); ++it)
    if(it->getAuthor()==author)
      cout<<"\t- "<<it->getContent()<<endl;
}
