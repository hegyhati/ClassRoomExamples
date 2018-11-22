#include "Post.hpp"


bool readPost(Post& p, istream& s){
  s>>p.likecount;
  if (s.fail()) return false;
  s>>p.author;
  if (s.fail()) return false;
  s>>p.content;
  if (s.fail()) return false;
  return true;
}

void writePost(const Post& p, ostream& s){
  s << p.author << ":"<<endl;
  s << "\t\"" << p.content << "\" - ["<<p.likecount<<"]\n\n";
}
