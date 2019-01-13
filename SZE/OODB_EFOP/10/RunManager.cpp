#include "RunManager.hpp"
#include <fstream>
#include "Run.hpp"

RunManager::RunManager(std::string databasefilename)
  :filename(databasefilename)
{
  Run tmp;
  std::ifstream inputfile(filename);
  while(!inputfile.eof()){
    tmp.loadfrom(inputfile);
    if(inputfile.good()) data.add(tmp);
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
  for(int i=0;i<data.size();i++)
    data[i].persist(outputfile);
  outputfile.close();
}

void RunManager::printAll(std::ostream& s) const
{
  s << "Runs stored in database - ["<<filename<<"]"<<std::endl;
  for(int i=0;i<data.size();i++)
    s << i+1 << ".: "<<data[i]<<std::endl;
}
