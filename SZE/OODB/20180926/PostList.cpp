#include "PostList.hpp"
#include <fstream>
#include <iostream>

void PostList::addPost(Post post){
  if(posts==NULL){
    posts=new PLItem;
    posts->data=post;
    posts->next=NULL;
  } else {
    PLItem *temp=posts;
    while(temp->next != NULL) temp=temp->next;
    temp->next=new PLItem;
    temp->next->data=post;
    temp->next->next=NULL;
  }
}

void PostList::popPost(){
  if(posts != NULL) {
    PLItem *temp=posts;
    posts=posts->next;
    delete temp;
  }
}

PostList::PostList(string filename) : posts(NULL) {
  ifstream posts(filename);
  while(! posts.eof()){
    addPost(Post(posts));
  }
}

PostList::~PostList(){
  while(posts!=NULL) popPost();
}

void PostList::printAll() const {
  cout<<"List of all posts:\n";
  for(PLItem* temp=posts; temp!=NULL; temp=temp->next)
    temp->data.print();
}


void PostList::printBy(string author)const {
  cout<<"Posts by "<<author<<":\n";
  for(PLItem* temp=posts; temp!=NULL; temp=temp->next)
    if(temp->data.getAuthor()==author)
      temp->data.print();
}
