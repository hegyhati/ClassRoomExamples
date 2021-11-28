from typing import NewType, Tuple, List
from random import shuffle

Card = NewType('Card', Tuple[int, int])
CardDeck = NewType('CardDeck', List[Card])

card_type = ['♠', '♣', '♡', '♢']
card_value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'D', 'K']


def to_string(card: Card) -> str:
    return '|' + card_value[card[1]] + card_type[card[0]]


def is_same_color(card1: Card, card2: Card) -> bool:
    return card1[0]//2 == card2[0]//2


def is_same_type(card1: Card, card2: Card) -> bool:
    return card1[0] == card2[0]


def is_same_value(card1: Card, card2: Card) -> bool:
    return card1[1] == card2[1]


def has_one_greater_value(card1: Card, card2: Card) -> bool:
    return card1[1] == card2[1] + 1


def get_shuffled_card_deck() -> CardDeck:
    deck = [(ctype, cvalue) for ctype in range(4) for cvalue in range(13)]
    shuffle(deck)
    return deck


def is_empty(deck: CardDeck) -> bool:
    return len(deck) == 0


def get_empty_deck() -> CardDeck:
    return []


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

def top_card(deck: CardDeck) -> Card:
    return deck[-1]


def push_card_to_deck(card: Card, deck: CardDeck, top:bool = True) -> None:
    if top:
        deck.append(card)
    else:
        deck.insert(0,card)


if __name__ == '__main__':
    l = get_shuffled_card_deck()
    for i in range(10):
        print_deck(l, visible=i)
        print()
