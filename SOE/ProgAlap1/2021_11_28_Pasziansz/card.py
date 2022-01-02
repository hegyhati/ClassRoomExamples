from typing import NewType, Tuple, List
from random import shuffle

Card = NewType('Card', Tuple[int, int])
CardDeck = NewType('CardDeck', List[Card])

card_type = ['♠', '♣', '♡', '♢']
card_value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'D', 'K']
# card_value = ['A', '2', '3']


def to_string(card: Card) -> str:
    """Returns the textual representation of a card
    Doesn't do safety checks on the input.

    Args:
        card (Card): The card in the form of a type-value int-int tuple.

    Returns:
        str: The textual representation: a pipe followed by the value then the type of the card.

    >>> to_string((0,0))
    '|A♠'
    >>> to_string((1,2))
    '|3♣'
    >>> to_string((3,10))
    '|J♢'
    """
    return '|' + card_value[card[1]] + card_type[card[0]]


def is_same_color(card1: Card, card2: Card) -> bool:
    """Returns whether the two cards are both red or black.

    Args:
        card1 (Card): the first card
        card2 (Card): the second card

    Returns:
        bool: True if they share the same color, False otherwise

    >>> is_same_color((0,0),(1,2))
    True
    >>> is_same_color((0,5),(2,9))
    False
    """
    return card1[0]//2 == card2[0]//2


def is_same_type(card1: Card, card2: Card) -> bool:
    return card1[0] == card2[0]


def is_same_value(card1: Card, card2: Card) -> bool:
    return card1[1] == card2[1]


def has_one_greater_value(card1: Card, card2: Card) -> bool:
    return card1[1] == card2[1] + 1


def get_shuffled_card_deck() -> CardDeck:
    deck:CardDeck = CardDeck([Card((ctype, cvalue)) for ctype in range(len(card_type)) for cvalue in range(len(card_value))])
    shuffle(deck)
    return deck


def is_empty(deck: CardDeck) -> bool:
    return len(deck) == 0


def get_empty_deck() -> CardDeck:
    return CardDeck([])


def print_deck(deck: CardDeck, visible: int = 1) -> None:
    if visible == 0:
        print('|'*len(deck) + '??', end='')
        return
    for idx, card in enumerate(deck):
        print('|' if idx < len(deck) - visible else to_string(card), end='')


def pop_top_card(deck: CardDeck) -> Card:
    card = deck[-1]
    del deck[-1]
    return card

def top_card(deck: CardDeck, count:int = 1) -> Card:
    return deck[-count]



def push_card_to_deck(card: Card, deck: CardDeck, top:bool = True) -> None:
    if top:
        deck.append(card)
    else:
        deck.insert(0,card)

def is_largest(card:Card)-> bool:
    return card[1] == len(card_value)-1
def is_smallest(card:Card)-> bool:
    return card[1] == 0

def get_type(card:Card) -> str:
    return card_type[card[0]] 

if __name__ == '__main__':
    l = get_shuffled_card_deck()
    for i in range(10):
        print_deck(l, visible=i)
        print()
