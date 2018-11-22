#ifndef POSTDATABASE_HPP
#define POSTDATABASE_HPP

#include "Post.hpp"
#include <fstream>
#include <string>
using namespace std;


#define SIZE 1024
struct PostDatabase{
  Post items[SIZE];
  int count;
};



// I/O functions

void readPosts(PostDatabase& posts, istream& file);
void writePosts(const PostDatabase& posts, ostream& s);


// Manipulations

void orderByLikes(PostDatabase& posts);
void removePostsBy(PostDatabase& posts, string bannedauthor="Jani");



#endif
