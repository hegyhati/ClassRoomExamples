#include "GPSRun.hpp"
#include "GPSMeasurement.hpp"
#include <fstream>
#include <cmath>

GPSRun::GPSRun() : Run("g")
{

}

void GPSRun::persist(std::ostream &s) const
{
  date.persist(s);
  s << "\t" << name << "\t" << gpxfilename << std::endl;
  std::ofstream outputfile(gpxfilename);
  for(int i=0;i<track.size();i++)
    track[i].persist(outputfile);
  outputfile.close();
}

void GPSRun::loadfrom(std::istream &s)
{
  date.loadfrom(s);
  s >> name;
  s >> gpxfilename;

  GPSMeasurement tmp;
  std::ifstream inputfile(gpxfilename);
  while(!inputfile.eof()){
    tmp.loadfrom(inputfile);
    if(inputfile.good()) track.add(tmp);
  }
  inputfile.close();
}

Time GPSRun::getDuration() const
{
  if (track.size()==0) return Time();
  else return track[track.size()-1].getTime()-track[0].getTime();
}

double GPSRun::getDistance() const
{
  double distance=0;
  for(int i=1;i<track.size();i++)
    distance += sqrt (
                  (track[i].getX()-track[i-1].getX())*(track[i].getX()-track[i-1].getX()) +
                  (track[i].getY()-track[i-1].getY())*(track[i].getY()-track[i-1].getY())
                  );
  return distance;
}

std::ostream &operator <<(std::ostream &s, const GPSRun &r)
{
  s << r.name
    << " (" << r.date << "):\t"
    <<r.getDistance()<<" km\t"
    <<r.getDuration();
  return s;
}
