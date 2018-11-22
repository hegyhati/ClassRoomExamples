#include <iostream>
#include <fstream>
using namespace std;

#include "PostDatabase.hpp"

int main(int argc, char** argv){
  
  ifstream postfile(argv[1]);
  ofstream fpostfile;
  if (argc>=3){
    fpostfile.open(argv[2]);
  }
   
  if (postfile.is_open()){
    PostDatabase posts;
       
    readPosts(posts,postfile);
   
    
    removePostsBy(posts,"Jani");
    orderByLikes(posts);
    
    writePosts(posts,fpostfile.is_open()?fpostfile:cout);
    
  } else {
    cerr << "Sorry bro' bad filename"<<endl;
  }

  return 0;
}
