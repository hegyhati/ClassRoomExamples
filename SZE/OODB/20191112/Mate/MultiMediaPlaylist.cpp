#include "MultiMediaPlaylist.h"
#include <iostream>
#include <algorithm>

#include "Music.h"
#include "Video.h"

MultiMediaPlaylist::MultiMediaPlaylist()
{
  
}

MultiMediaPlaylist::MultiMediaPlaylist(const MultiMediaPlaylist &other)
{
  for(const Media* track: other.tracks){
    auto music = dynamic_cast<const Music*>(track);
    if (music!=nullptr) add(new Music(*music));
    auto video = dynamic_cast<const Video*>(track);
    if (video!=nullptr) add(new Video(*video));
  }
}

MultiMediaPlaylist::~MultiMediaPlaylist()
{
  for(auto pMedia:tracks)
     delete pMedia;
  tracks.clear();
}

const Media *MultiMediaPlaylist::current() const
{
  if(tracks.empty()) return nullptr;
  else return tracks.front();
}

void MultiMediaPlaylist::add(Media * newtrack)
{
  tracks.push_back(newtrack);
}

void MultiMediaPlaylist::skip()
{
  if(!tracks.empty()) {
    delete tracks.front();
    tracks.pop_front();
  }
}

void MultiMediaPlaylist::sortByLength()
{
 tracks.sort(Media::compareByDuration);
}

void MultiMediaPlaylist::sortByTitle()
{
  tracks.sort(Media::compareByTitle);
}

void MultiMediaPlaylist::print() const
{
  std::cout << "Playlist contents:" << std::endl;
  int num=0;
  for(auto it:tracks) {
    std::cout << "  " << num << " - ";
    it->print();
    std::cout << std::endl;
    num++;
  }
}
