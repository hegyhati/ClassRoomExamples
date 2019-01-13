#include "RunManager.hpp"
#include <fstream>
#include "ManualRun.hpp"

RunManager::RunManager(std::string databasefilename)
  :filename(databasefilename)
{
  std::string type;
  std::ifstream inputfile(filename);

  while(!inputfile.eof()){
    inputfile >> type;
    if(inputfile.good()) {
      if (type=="m") {
        ManualRun* tmp = new ManualRun;
        tmp->loadfrom(inputfile);
        data.add(tmp);
      } else if (type=="g") {
        GPSRun* tmp = new GPSRun;
        tmp->loadfrom(inputfile);
        data.add(tmp);
      }
    }
  }
  inputfile.close();
}

RunManager::~RunManager()
{
  persist();
}

void RunManager::persist() const
{
  std::ofstream outputfile(filename);
  for(int i=0;i<data.size();i++) {
    outputfile << " " << data[i]->getType() << " ";
    data[i]->persist(outputfile);
  }
  outputfile.close();
}

void RunManager::printAll(std::ostream& s) const
{
  s << "Runs stored in database - ["<<filename<<"]"<<std::endl;
  for(int i=0;i<data.size();i++) {
    s << i+1 << ".: ";
    if (dynamic_cast<ManualRun*>(data[i]) != nullptr)
      s << *dynamic_cast<ManualRun*>(data[i]);
    if (dynamic_cast<GPSRun*>(data[i]) != nullptr)
      s << *dynamic_cast<GPSRun*>(data[i]);
    s <<std::endl;
  }
}
