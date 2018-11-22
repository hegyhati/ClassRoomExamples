#ifndef POST_HPP
#define POST_HPP

#include <string>
#include <fstream>
using namespace std;

struct Post{
  string author;
  string content;
  int likecount;
};

bool readPost(Post& p, istream& s);

void writePost(const Post& p, ostream& s);

#endif
