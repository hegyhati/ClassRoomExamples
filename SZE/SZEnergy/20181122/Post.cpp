#include "Post.hpp"


bool operator>>(istream& s, Post& post){
  s>>post.likecount;
  if (s.fail()) return false;
  s>>post.author;
  if (s.fail()) return false;
  s>>post.content;
  if (s.fail()) return false;
  return true;
}

ostream& operator<<(ostream& s, const Post& post) {
  s << post.author << ":"<<endl;
  s << "\t\"" << post.content << "\" - ["<<post.likecount<<"]\n\n";
  return s;
}

int Post::getLikeCount() const {return likecount;}
string Post::getAuthor() const {return author;}
