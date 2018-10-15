#include "Post.hpp"
#include <iostream>


Post::Post(int id, string author, string content)
  :id(id),author(author),content(content) {}


void checkFileStatus(ifstream& file){
  if (file.rdstate() != std::ios_base::goodbit)
  throw string("End of file reached");
}

int fetchid(ifstream& file){
  int toReturn;
  file>>toReturn;
  checkFileStatus(file);
  return toReturn;
}

string fetchstring(ifstream& file){
  string temp;  
  getline(file,temp,'"');
  getline(file,temp,'"');
  checkFileStatus(file);  
  return temp;
}


Post::Post(ifstream& file)
  :id(fetchid(file)),author(fetchstring(file)),content(fetchstring(file)) {}

string Post::getAuthor() const {return author;}

string Post::getContent() const {return content;}

int Post::getId() const {return id;}

ostream& operator<<(ostream& file, const Post& post){
  file<<post.getId()<<" "
      <<"\""<<post.getAuthor()<<"\" "
      <<"\""<<post.getContent()<<"\""
      <<endl;
  return file;
}
