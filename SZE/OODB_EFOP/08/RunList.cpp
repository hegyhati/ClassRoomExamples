#include "RunList.hpp"
#include <fstream>

RunList::~RunList(){
  for(RunListElement *tmp; head!=nullptr; head=tmp){
    tmp=head->next;
    delete head;    
  }
}

    
std::istream& operator >> (std::istream&  s, RunList& rl) {
  Run tmprun;
  do {    
    s >> tmprun;
    if (tmprun.getDistance()!=0 && tmprun.getDuration() !=0) {
      RunList::RunListElement* tmp=new RunList::RunListElement;
      tmp->data=tmprun;
      tmp->next=rl.head;
      rl.head=tmp;
    }
  } while (tmprun.getDistance()!=0 && tmprun.getDuration() !=0);
  return s;
}

void RunList::loadfrom(std::string filename) {
  std::ifstream input(filename);
  input >> *this;
  input.close();
}

std::ostream& operator << (std::ostream&  s, const RunList& rl) {
  for(RunList::RunListElement* tmp=rl.head;tmp!=nullptr;tmp=tmp->next){
    s<< (tmp->data) << std::endl;
  }
  return s;
}

void RunList::persist(std::string filename) const{
  std::ofstream output(filename);
  for(RunListElement* tmp=head;tmp!=nullptr;tmp=tmp->next){
    tmp->data.persist(output);
  }
  output << "Enough 0 0"<<std::endl;
  output.close();
}


int RunList::size() const {
  int size=0;
  for(RunListElement* tmp=head;tmp!=nullptr;tmp=tmp->next) size++;
  return size;
}

Run RunList::operator [] (int idx) const {
  if (idx < 0 || idx >= size()) return Run("Error");
  RunListElement* tmp=head;
  while(idx!=0) {
    tmp=tmp->next;
    idx--;
  }
  return tmp->data;
}



