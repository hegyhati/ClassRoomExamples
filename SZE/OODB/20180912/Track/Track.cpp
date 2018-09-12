#include "Track.hpp"
#include <iostream>
using namespace std;

Track::Track() : track(NULL){}

Track::~Track() {
  if(track==NULL) return;
  else {
    PLItem* temp2;
    for(PLItem* temp=track; temp!=NULL; temp=temp2) {
      temp2=temp->next;
      delete temp;
    }
  }
  track=NULL;
}

void Track::append(double x, double y, double t) {
  if(track==NULL){
    track = new PLItem;
    track->point.set(x,y,t);
    track->next=NULL;
  } else {
    PLItem* temp=track;
    while(temp->next!=NULL) temp=temp->next;
    temp->next = new PLItem;
    temp->next->point.set(x,y,t);
    temp->next->next=NULL;
  }
}



void Track::print() const {
  for(PLItem* temp=track; temp!=NULL; temp=temp->next){
    temp->point.print();
    cout<<" -> ";
  }
  cout << endl;
}


double Track::length() const {
  if(track==NULL || track->next==NULL) return 0;
  double sum=0;
  for(PLItem* temp=track; temp->next!=NULL; temp=temp->next){
    sum += temp->point.distanceFrom(temp->next->point);
  }
  return sum;
}


