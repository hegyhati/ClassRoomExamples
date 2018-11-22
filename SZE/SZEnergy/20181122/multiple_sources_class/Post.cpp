#include "Post.hpp"


bool Post::readFrom(istream& s){
  s>>likecount;
  if (s.fail()) return false;
  s>>author;
  if (s.fail()) return false;
  s>>content;
  if (s.fail()) return false;
  return true;
}

void Post::writeTo(ostream& s) const {
  s << author << ":"<<endl;
  s << "\t\"" << content << "\" - ["<<likecount<<"]\n\n";
}



int Post::getLikeCount() const {return likecount;}
string Post::getAuthor() const {return author;}
