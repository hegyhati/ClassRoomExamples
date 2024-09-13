from collections.abc import Iterable
import random
from enum import Enum

class Suit(Enum):
    SPADES   = "♠"
    CLUBS    = "♣"
    DIAMONDS = "♦"
    HEARTS   = "♥"
    
class Color(Enum):
    BLACK = 0
    RED   = 1
        

RANK_COUNT = 13

def color(suit:Suit) -> Color:
    match suit:
        case Suit.SPADES | Suit.CLUBS: return Color.BLACK
        case Suit.DIAMONDS | Suit.HEARTS: return Color.RED

        

class Card:
   
    BACK_DISPLAY = "🂠"       
    __display = {
        Suit.SPADES   : "🂡🂢🂣🂤🂥🂦🂧🂨🂩🂪🂫🂭🂮",
        Suit.CLUBS    : "🃑🃒🃓🃔🃕🃖🃗🃘🃙🃚🃛🃝🃞",
        Suit.DIAMONDS : "🃁🃂🃃🃄🃅🃆🃇🃈🃉🃊🃋🃍🃎",
        Suit.HEARTS   : "🂱🂲🂳🂴🂵🂶🂷🂸🂹🂺🂻🂽🂾"
    }    
    
    def __init__(self, suit:Suit, rank:int) -> None:
        if rank < 0 or rank > RANK_COUNT: raise ValueError(f"Wrong rank: {rank}")
        self._suit = suit
        self._rank = rank    
    
    def __str__(self):
        return ("\033[1;31m" if self.color() == Color.RED else "\033[1;m") + self.__display[self._suit][self._rank] + "\033[0m"
 
    def color(self) -> Color:
        return  color(self._suit)
    
    def is_ace(self) -> bool:
        return self._rank == 0
    
    def is_king(self) -> bool:
        return self._rank == RANK_COUNT-1
    
    def get_suit(self) -> Suit:
        return self._suit
    
    def get_rank(self) -> int:
        return self._rank
    
    @staticmethod
    def same_color(card1:"Card", card2:"Card") -> bool:
        return card1.color() == card2.color()


class Deck:
    def __init__(self, full:bool = True, shuffled:bool = True) -> None:
        self.__deck : list[Card] = []
        
    @staticmethod
    def full_deck(shuffled:bool = True) -> "Deck":
        fulldeck = Deck()
        fulldeck.__deck = [ Card(suit,rank) for suit in Suit for rank in range(RANK_COUNT) ] 
        if shuffled: fulldeck.shuffle()
        return fulldeck
    
    @staticmethod
    def deck_from_cards(cards: Iterable[Card], shuffled:bool = False) -> "Deck":
        deck = Deck()
        deck.__deck = list(cards)
        if shuffled: deck.shuffle()
        return deck
    
    def shuffle(self) -> None:
        random.shuffle(self.__deck)
    
    def is_empty(self):
        return len(self.__deck) == 0
    
    def is_full(self):
        return len(self.__deck) == RANK_COUNT * len(Suit)

    def peek_top(self) -> Card:
        return self.__deck[-1]
    
    def peek_bottom(self) -> Card:
        return self.__deck[0]
    
    def pick_top(self) -> Card:
        return self.__deck.pop()
    
    def put_top(self, card:Card) -> None:
        self.__deck.append(card)
    
    def size(self) -> int:
        return len(self.__deck)
        
    def __str__(self):
        return " ".join([ str(card) for card in self.__deck ])
    
    
if __name__ == "__main__":
    d = Deck.full_deck()
    print(d)
    for _ in range(42):
        print(f"Pop {d.pick_top()}")
    print(d)


    
    
    
    
        
    