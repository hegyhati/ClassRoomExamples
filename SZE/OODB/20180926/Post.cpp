#include "Post.hpp"
#include <iostream>


Post::Post(string author, string content)
  :author(author),content(content) {}
  

string fetchstring(ifstream& file){
  string temp;
  getline(file,temp,'"');
  getline(file,temp,'"');
  return temp;
}


Post::Post(ifstream& file)
  :author(fetchstring(file)),content(fetchstring(file)) {}

void Post::print() const {
  cout<<author<<": "<<content<<endl<<endl;
}

string Post::getAuthor() const {return author;}

string Post::getContent() const {return content;}
