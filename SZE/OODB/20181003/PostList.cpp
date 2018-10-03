#include "PostList.hpp"
#include <fstream>
#include <iostream>



PostList::PostList(string filename) {
  ifstream postfile(filename);
  while(! postfile.eof()){
    try{      
      posts.add(Post(postfile));
    } catch (string e) {
      cerr << "Sorry, reading post was unsuccessful...\n";
      cerr << "Error message: "<<e<<endl;
    }
  }
}

void PostList::printAll() const {
  cout<<"List of posts:\n";
  posts.printAll();
}


void PostList::printBy(string author)const {
  cout<<"Posts by "<<author<<":\n";
  for(int i=0; i<posts.size();i++)
    if(posts.getElement(i).getAuthor()==author)
      cout<<"\t- "<<posts.getElement(i).getContent()
          <<endl;
}
