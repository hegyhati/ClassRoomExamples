import datetime
# necessary imports

class Bucket:
    def __init__(self, capacity:float) -> None:
        """_summary_

        Args:
            capacity (float): capacity of the bucket

        Raises:
            ValueError: if capacity is 0 or negative
        """
    
    def get_level(self) -> float:
        """Returns the amount of water in the bucket."""
    
    def get_capacity(self) -> float:
        """Returns the maximal capacity of the bucket."""

    def get_remaining_capacity(self) -> float:
        """Returns the remaining free capacity of the bucket."""
    
    def empty(self) -> None:
        """Empties the bucket."""
    
    def fill(self) -> None:
        """Fills the bucket fully."""

    def pour_into(self, other:"Bucket"):
        """Pours water from this bucket to another until that bucket is full, or this runs out of water.

        Args:
            other (Bucket): the sink
        """

class BucketSystem:
    def __init__(self) -> None:
        """Initializer"""
    
    def add_bucket(self, capacity:float) -> None:
        """Adds a new empty bucket to the system.

        Args:
            capacity (float): capacity of the new bucket.
        """
    
    def bucket_count(self) -> int:
        """Returns the number of buckets in the system."""

    def empty_buckets(self, buckets:list[int]) -> None:
        """Empty all given buckets if all of the indices are valid.

        Args:
            buckets (list[int]): list of indices of buckets

        Raises:
            ValueError: if any of the indices are incorrect
        """

    def fill_buckets(self, buckets:list[int]) -> None:
        """Fills all given buckets if all of the indices are valid.

        Args:
            buckets (list[int]): list of indices of buckets

        Raises:
            ValueError: if any of the indices are incorrect
        """
    
    def pour(self, source:int, sink:int) -> None:
        """Pours from one bucket to another.

        Args:
            source (int): the index of the source bucket
            sink (int): the index of the sink bucket

        Raises:
            ValueError: if any of the indices are invlaid
            ValueError: if the source and the sink are the same
        """

    def get_levels(self) -> list[tuple[float,float]]:
        """Returns he used and the available capacity of all buckets.

        Returns:
            list[tuple[float,float]]: list of (current usage,maximal capacity) pairs for each bucket
        """
    
    def has_volume(self, volume:float) -> bool:
        """Returns whether any of the buckets hold exactly this capacity."""

CHALLENGEDIR = "challenges" # directory where challenge files are located
GAMEDIR = "games" # directory where games should be saved

class Game:
    def __init__(self, capacities:list[float], goal:float, steplimit:int) -> None:
        self.__goal = goal
        self.__maxsteps = steplimit
        self.__step_counter = 0
        self.__buckets = BucketSystem()
        for capacity in capacities:
            self.__buckets.add_bucket(capacity)
        
    def __str__(self):
        return "\n".join([
            f"Goal: {self.__goal}",
            f"Steps remaining: {self.__maxsteps - self.__step_counter}",
            "Buckets:",
            *[f" - {idx}: {level}/{capacity}" for idx,(level,capacity) in enumerate(self.__buckets.get_levels())]
        ])
    
    def __export_state(self):
        """Generates a jpg from a bar plot showing the state of the game.
        Filename has the format: GAMEDIR/startdatetime/step.jpg
        """


    def run(self) -> bool:
        """Starts running the game"""
        self.__game_start = datetime.datetime.now().isoformat()
        # make GAMEDIR/startdatetime dir
        
        # game lasts while the player still has steps and the challnge is not solved.

        # each iteration starts with displaying the state of the game (bucket levels, steps remaining) then ask for the next step with:
        """
                What do you want to do?
                 - ABORT
                 - FILL bucket1 bucket2 ...
                 - EMPTY bucket1 bucket2 ...
                 - POUR source_bucket sink_bucket
                Your command:
        """
        # report if the command is invalid
        # report if the arguments (indeces) are invalid
        # if both are ok, execute the step and increase the step counter
        # if the target volume is reached or the step limit is reached, return True or False after a message respectively
        # if not, start another round
    

if __name__ == "__main__":
    print("Which challenge do you want to play?")
    # list all the avialable challenges in CHALLENGEDIR without the .json
    # if the response is invalid, report it, and exit the program
    # otherwise, open the challenge, create a game, and run it.
    
    

    

    


        

    


