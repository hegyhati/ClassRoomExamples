#include "GPSMeasurementList.hpp"
#include <fstream>

GPSMeasurementList::~GPSMeasurementList(){
  for(GPSMeasurementListElement *tmp; head!=nullptr; head=tmp){
    tmp=head->next;
    delete head;
  }
}

void GPSMeasurementList::add(GPSMeasurement GPSMeasurement)
{
  if (head==nullptr) {
    head = new GPSMeasurementListElement;
    head ->data=GPSMeasurement;
    head ->next=nullptr;
  } else {
    GPSMeasurementListElement *tmp=head;
    while(tmp->next!=nullptr) tmp=tmp->next;
    tmp->next=new GPSMeasurementListElement;
    tmp->next ->data=GPSMeasurement;
    tmp->next ->next=nullptr;
  }
}


int GPSMeasurementList::size() const {
  int size=0;
  for(GPSMeasurementListElement* tmp=head;tmp!=nullptr;tmp=tmp->next) size++;
  return size;
}

GPSMeasurement GPSMeasurementList::operator [] (int idx) const {
  if (idx < 0 || idx >= size()) return GPSMeasurement();
  GPSMeasurementListElement* tmp=head;
  while(idx!=0) {
    tmp=tmp->next;
    idx--;
  }
  return tmp->data;
}




