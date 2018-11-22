#include <iostream>
#include <fstream>
#include <string>
using namespace std;

#define SIZE 1024

struct Post{
  string author;
  string content;
  int likecount;
};

bool readPost(Post& p, istream& s){
  s>>p.likecount;
  if (s.fail()) return false;
  s>>p.author;
  if (s.fail()) return false;
  s>>p.content;
  if (s.fail()) return false;
  return true;
}



int readPosts(Post posts[SIZE], istream& file){
  int postcount=0;
  while(!file.eof()) {
    if(readPost(posts[postcount],file)) {
      postcount++;
    } else {
      /* Handle bad input */
    }
  }
  return postcount;
}


void writePost(const Post& p, ostream& s){
  s << p.author << ":"<<endl;
  s << "\t\"" << p.content << "\" - ["<<p.likecount<<"]\n\n";
}


void writePosts(const Post posts[SIZE], int postcount, ostream& s){
  for(int p=0; p<postcount; ++p) {
    writePost(posts[p],s);
  }
}


void orderByLikes(Post posts[SIZE], int postcount){
  for(int i=0;i<postcount-1;++i){
    for(int p=0;p<postcount-i-1;++p){
      if(posts[p].likecount < posts[p+1].likecount){
        Post temp;
        temp=posts[p+1];
        posts[p+1]=posts[p];
        posts[p]=temp;
      }
    }
  }
}


void removePostsBy(Post posts[SIZE], int& postcount, string bannedauthor){
  for(int p=postcount-1;p>=0;--p) {
    if(posts[p].author==bannedauthor){
      for(int p2=p+1;p2<postcount;++p2){
        posts[p2-1]=posts[p2];
      }
      --postcount;
    }
  }
}

int main(int argc, char** argv){
  
  ifstream postfile(argv[1]);
  ofstream fpostfile;
  if (argc>=3){
    fpostfile.open(argv[2]);
  }
   
  if (postfile.is_open()){
    Post posts[SIZE];
    int postcount=0;
       
    postcount = readPosts(posts,postfile);
   
    
    removePostsBy(posts,postcount,"Jani");
    orderByLikes(posts,postcount);
    
    writePosts(posts,postcount,fpostfile.is_open()?fpostfile:cout);
    
  } else {
    cerr << "Sorry bro' bad filename"<<endl;
  }

  return 0;
}
