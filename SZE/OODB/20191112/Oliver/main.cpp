#include <iostream>

#include "Music.h"
#include "Video.h"
#include "MultiMediaPlaylist.h"

int main() {
    MultiMediaPlaylist pl;
    pl.add(new Music("Foobar Fighters", "The Preprocessor", 269));
    pl.add(new Video("Ricky and Mort S04E01", 1320, 1920, 1080));
    pl.print();

    std::cout << "Currently playing: ";
    pl.current()->print();

    pl.add(new Music("Rage Against The Computer", "Nulls On Parade", 230));
    pl.sortByLength();
    std::cout << "After sortByLength(): \n";
    pl.print();
    pl.sortByTitle();
    std::cout << "After sortByTitle(): \n";
    pl.print();


    std::cout << "Current playback finished: ";
    pl.current()->print();
    pl.skip();
    std::cout << "Next up: ";
    pl.current()->print();
    pl.print();

    // +1 tests
    
    std::cout << "Test cout << " << *pl.current() << "\n"
        << Music("Metal Woman", "Phantom Of The Operator", 441) << "\n\n";

    MultiMediaPlaylist *copy = new MultiMediaPlaylist(pl);
    copy->skip();
    copy->skip();
    copy->print();
    delete copy;
    

    pl.print();
    pl.skip();
    pl.print();
    pl.skip();
    std::cout << "TEST: Playlist should be empty now:\n";
    pl.print();
    pl.skip(); // do nothing
    if (pl.current()) {
        std::cerr << "TEST FAILED: current() should return nullptr for empty playlist\n";
    }
    
    return 0;
}