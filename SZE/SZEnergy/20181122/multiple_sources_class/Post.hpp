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
    bool readFrom(istream& s);
    void writeTo(ostream& s) const;
    int getLikeCount() const;
    string getAuthor() const;
};





#endif
