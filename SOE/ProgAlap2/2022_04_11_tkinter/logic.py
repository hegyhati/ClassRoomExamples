from multiprocessing.sharedctypes import Value


class Deck:
    def __init__(self, cards, hidden) -> None:
        self.cards = cards[:]
        self.hidden = hidden
    def can_push(self, new_card) -> bool:
        return new_card == self.cards[-1] -1
    def push(self, new_card) -> None:
        if self.can_push(new_card):
            self.cards.append(new_card)
        else:
            raise ValueError