def pretty_length(s:int) -> str:
    if s > 3600:
        return f"{s//3600}:{s%3600//60:02}:{s%60:02}"
    elif s > 60:
        return f"{s//60}:{s%60:02}"
    else:
        return f"{s%60}"

class Track:
    def __init__(...) -> None:
        pass

    def __str__(self) -> str:
        pass  

    def get_length(self) -> int:
        pass
    
    def is_from_genre(self, genre:str):
        pass


class PlayQueue:
    
    """
    Maybe missing methods.
    """      

    def total_length(self) -> str:
        pass

    def is_from_genre(self, genre:str):
        pass
    
    def next_track(self):
        pass


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
