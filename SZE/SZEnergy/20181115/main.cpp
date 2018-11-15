#include <iostream>
#include <fstream>
#include <string>
using namespace std;

struct Post{
  string author;
  string content;
};

bool read(Post& p, istream& s){
  s>>p.author;
  s>>p.content;
  return !s.fail();
}

void write(const Post& p, ostream& s){
  s << p.author << ":"<<endl;
  s << "\t\"" << p.content << "\"\n\n";
}

int main(int argc, char** argv){
  Post post;
  ifstream postfile(argv[1]);
  ofstream fpostfile;
  if (argc>=3){
    fpostfile.open(argv[2]);
  }
   
  if (postfile.is_open()){    
    while(!postfile.eof()) {
      if(read(post,postfile)) {
        write(post,fpostfile.is_open()?fpostfile:cout);
      }
    }
  } else {
    cerr << "Sorry bro' bad filename"<<endl;
  }
}
