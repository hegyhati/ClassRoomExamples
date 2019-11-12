#include "MultiMediaPlaylist.h"

#include <algorithm>
#include <iostream>

#include "Music.h"
#include "Video.h"

MultiMediaPlaylist::MultiMediaPlaylist(const MultiMediaPlaylist& other)
{
    for (Media* p : other.playlist) {
        const Video* vp = dynamic_cast<const Video*>(p);
        if (vp) {
            add(new Video(*vp));
        }
        else if (const Music* mp = dynamic_cast<const Music*>(p)) {
            add(new Music(*mp));
        }
    }
}

MultiMediaPlaylist::~MultiMediaPlaylist()
{
    for (Media* p : playlist)
        delete p;
}

const Media* MultiMediaPlaylist::current() const
{
    return playlist.empty() ? nullptr : playlist.front();
}

void MultiMediaPlaylist::add(Media* media)
{
    playlist.push_back(media);
}

void MultiMediaPlaylist::skip()
{
    if (!playlist.empty()) {
        delete playlist.front();
        playlist.pop_front();
    }
}

void MultiMediaPlaylist::sortByLength()
{
    std::sort(playlist.begin(), playlist.end(),
        [](const Media* a, const Media* b) { return a->getLength() < b->getLength(); }
    );
}

void MultiMediaPlaylist::sortByTitle()
{
    std::sort(playlist.begin(), playlist.end(),
        [](const Media* a, const Media* b) { return a->getTitle() < b->getTitle(); }
    );
}

void MultiMediaPlaylist::print() const
{
    std::cout << "Playlist contents:\n";
    int i = 0;
    for (Media* p : playlist) {
        std::cout << "  " << i++ << " - ";
        p->print();
    }
}
