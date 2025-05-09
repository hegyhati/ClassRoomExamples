class Track:
    def __init__(...) -> None:
        """Initializes

        Args:
            artist (str): name of artist
            title (str): the title
            length_in_seconds (int): the duration of the track in seconds
            genre (str, optional): the genre, only optional.
        """
        pass

    def __str__(self) -> str:
        """gives a string representation

        Returns:
            str: format: artist: title (length)
        """

    def pretty_length(self) -> None:
        """Provides a pretty string representation of length"""
        s = self.__seconds
        if s > 3600:
            return f"{s//3600}:{s%3600//60:02}:{s%60:02}"
        elif s > 60:
            return f"{s//60}:{s%60:02}"
        else:
            return f"{s%60}"

    def get_length(self) -> int:
        """Returns the length in seconds"""
        pass

    
    def is_from_genre(self, genre:str):
        """Returns whether the track belongs to the given genre or not. Partial match is also a match, "heavy metal" is "metal", but "metal" is not "heavy metal"."""
        pass


class Playlist:
    def __init__(self, unique:bool) -> None:
        """Initializer

        Args:
            unique (bool): whether the same track is allowed multiple times on the list
        """
        pass

    def add_track(self, track: Track) -> None:
        """Adds track to the end of the list. Unless the list is unique and the same track is already there."""
        pass

    def total_length(self) -> int:
        """Returns the total length of the playlist in seconds."""
        pass

    def is_from_genre(self, genre:str):
        """Returns if all of the tracks on the list are from this genre."""
        pass
    
    def print(self):
        for idx, track in enumerate(self.__tracks):
            print(f"{idx+1:2}. {track}")

def metal_test():
    metal:Playlist = Playlist(False)    
    metal.add_track(Track("Metallica", "Master of Puppets", 514, "thrash metal"))
    metal.add_track(Track("Iron Maiden", "The Trooper", 244, "heavy metal"))
    metal.add_track(Track("Metallica", "One", 447, "heavy metal"))
    metal.add_track(Track("Stratovarius", "Hunting High and Low", 259, "power metal"))
    metal.add_track(Track("Iron Maiden", "Fear of the Dark", 438, "heavy metal"))
    metal.add_track(Track("Children of Bodom", "Are You Dead Yet?", 231, "melodic death metal"))
    metal.add_track(Track("Stratovarius", "Black Diamond", 317, "power metal"))
    
    metal.print()
    print(f"My playlist {'is' if metal.is_from_genre('metal') else 'is not'} metal, total length: {metal.total_length()} seconds")
    
    metal.add_track(Track("Haggard", "Awaking the Centuries", 563, "symphonic metal"))
    metal.add_track(Track("Haggard", "Eppur Si Muove", 430, "symphonic metal"))
    metal.add_track(Track("Electric Callboy", "Hypa Hypa", 182, "electronicore"))
    metal.add_track(Track("Electric Callboy", "Pump It", 204, "electronicore"))
    
    metal.print()
    print(f"My playlist {'is' if metal.is_from_genre('metal') else 'is not'} metal, total length: {metal.total_length()} seconds")

def rock_test():
    highway_to_hell = Track("AC/DC", "Highway to Hell", 208)
    back_in_black = Track("AC/DC", "Back in Black", 255)
    stairway_to_heaven = Track("Led Zeppelin", "Stairway to Heaven", 482)
    bohemian_rhapsody = Track("Queen", "Bohemian Rhapsody", 354)
    paint_it_black = Track("The Rolling Stones", "Paint It Black", 200)
    smells_like_teen_spirit = Track("Nirvana", "Smells Like Teen Spirit", 301)
    smoke_on_the_water = Track("Deep Purple", "Smoke on the Water", 340)    
    
    rock:Playlist = Playlist(True)
    rock.add_track(highway_to_hell)
    rock.add_track(bohemian_rhapsody)
    rock.add_track(smoke_on_the_water)
    rock.add_track(stairway_to_heaven)
    rock.add_track(smells_like_teen_spirit)
    rock.add_track(highway_to_hell)
    rock.add_track(back_in_black)
    rock.add_track(paint_it_black)
    rock.add_track(smells_like_teen_spirit)

    rock.print()
    print(f"My playlist {'is' if rock.is_from_genre('pop') else 'is not'} pop, total length: {rock.total_length()} seconds")


if __name__ == "__main__":
    metal_test()
    rock_test()