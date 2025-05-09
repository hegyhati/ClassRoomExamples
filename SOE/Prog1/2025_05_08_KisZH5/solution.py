def pretty_length(s:int) -> str:
    if s > 3600:
        return f"{s//3600}:{s%3600//60:02}:{s%60:02}"
    elif s > 60:
        return f"{s//60}:{s%60:02}"
    else:
        return f"{s%60}"

class Track:
    def __init__(self, artist: str, title: str, length_in_seconds: int, genre:str = "") -> None:
        self.__artist = artist
        self.__title = title
        self.__seconds = length_in_seconds
        self.__genre = genre

    def __str__(self) -> str:
        return f"{self.__artist}: {self.__title} ({pretty_length(self.__seconds)})"    

    def get_length(self) -> int:
        return self.__seconds
    
    def is_from_genre(self, genre:str):
        return genre in self.__genre


class PlayQueue:
    def __init__(self) -> None:
        self.__queue:list[Track]  = []
    
    def __str__(self) -> str:
        match self.__queue:
            case []: return "The play queue is empty."
            case [track]: return f"Playing the last track in the queue: {track}"
            case [current, *rest]: return f"Playing {current}, {len(rest)} more tracks."

    def add_track(self, track: Track) -> None:
        self.__queue.append(track)        

    def total_length(self) -> str:
        return pretty_length(sum(track.get_length() for track in self.__queue))

    def is_from_genre(self, genre:str):
        return all(track.is_from_genre(genre) for track in self.__queue)
    
    def next_track(self):
        if len(self.__queue) != 0:
            del self.__queue[0]


if __name__ == "__main__":   
    pq:PlayQueue = PlayQueue()    
    pq.add_track(Track("Electric Callboy", "Hypa Hypa", 182, "electronicore"))
    pq.add_track(Track("Metallica", "Master of Puppets", 514, "thrash metal"))
    pq.add_track(Track("Iron Maiden", "The Trooper", 244, "heavy metal"))
    pq.add_track(Track("Metallica", "One", 447, "heavy metal"))
    pq.add_track(Track("Stratovarius", "Hunting High and Low", 259, "power metal"))
    pq.add_track(Track("Children of Bodom", "Are You Dead Yet?", 231, "melodic death metal"))
    
    print(pq)
    print(f"My queue {'is' if pq.is_from_genre('metal') else 'is not'} metal")

    print("\nSkip track...\n")
    pq.next_track()

    print(pq)
    print(f"My queue {'is' if pq.is_from_genre('metal') else 'is not'} metal")
    print(f"Total length: {pq.total_length()}")
    
    print("\nAdd 3 more tracks...\n")
    pq.add_track(Track("Iron Maiden", "Fear of the Dark", 438))
    pq.add_track(Track("Stratovarius", "Black Diamond", 317))
    pq.add_track(Track("Haggard", "Awaking the Centuries", 563))
    
    print(pq)
    print(f"Total length: {pq.total_length()}")

    print("\n Skip all the tracks one by one...\n")

    while pq.total_length() != "0":
        pq.next_track()
        print("Track skipped...", pq, pq.total_length())

    pq.next_track()
    print("(No) track skipped...", pq, pq.total_length())
