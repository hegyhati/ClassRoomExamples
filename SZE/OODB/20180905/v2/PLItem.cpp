#include "PLItem.hpp"
#include <iostream>
using namespace std;

void append(PLItem*& track, Point p){
  if(track==NULL){
    track = new PLItem;
    track->p=p;
    track->next=NULL;
  } else {
    PLItem* temp=track;
    while(temp->next!=NULL) temp=temp->next;
    temp->next = new PLItem;
    temp->next->p=p;
    temp->next->next=NULL;
  }
}

void print(PLItem* track){
  for(PLItem* temp=track; temp!=NULL; temp=temp->next){
    cout<<"("<<temp->p.x<<","<<temp->p.y<<")["<<temp->p.t<<"] -> ";
  }
  cout << endl;
}

void reset(PLItem*& track){
  if (track!=NULL){
    reset(track->next);
    delete track;
    track=NULL;
  }
}

double length(PLItem* track){
  if(track==NULL || track->next==NULL) return 0;
  double sum=0;
  for(PLItem* temp=track; temp->next!=NULL; temp=temp->next){
    sum += distance(temp->p,temp->next->p);
  }
  return sum;
}

double avgspeed(PLItem* track){
  if(track==NULL || track->next==NULL) return -1;
  double tstart=track->p.t;
  double tend;
  for(PLItem* temp=track; temp!=NULL; temp=temp->next)
    tend=temp->p.t;
  return length(track)/(tend-tstart);
}
