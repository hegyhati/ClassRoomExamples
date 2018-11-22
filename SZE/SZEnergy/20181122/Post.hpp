#ifndef POST_HPP
#define POST_HPP

#include <string>
#include <fstream>
using namespace std;

class Post{
  private:
    string author;
    string content;
    int likecount;
  public:
    int getLikeCount() const;
    string getAuthor() const;

    friend ostream& operator<<(ostream& s, const Post& post);
    friend bool operator>>(istream& s, Post& post);
};

#endif
