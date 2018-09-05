#include <iostream>
#include <cmath>

using namespace std;

struct Point{
  double x;
  double y;
  double t;
};

double distance(Point p1, Point p2){
  return sqrt((p1.x-p2.x)*(p1.x-p2.x)+(p1.y-p2.y)*(p1.y-p2.y));
}

struct PLItem {
  Point p;
  PLItem* next;
};

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

int main(){
  PLItem* track=NULL;
  append(track,{1,1,0});
  append(track,{4,5,30});
  append(track,{6,5,40});
  print(track);
  cout<<"Length: "<<length(track)<<endl;
  cout<<"AVG Speed: "<<avgspeed(track)<<endl;
  reset(track);
}
