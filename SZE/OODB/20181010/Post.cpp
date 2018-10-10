#include "Post.hpp"
#include <iostream>


Post::Post(string author, string content)
  :author(author),content(content) {}
  

string fetchstring(ifstream& file){
  string temp;
  
  getline(file,temp,'"');
  getline(file,temp,'"');
  if (file.rdstate() != std::ios_base::goodbit)
  throw string("End of file reached");
  
  return temp;
}


Post::Post(ifstream& file)
  :author(fetchstring(file)),content(fetchstring(file)) {}

string Post::getAuthor() const {return author;}

string Post::getContent() const {return content;}
