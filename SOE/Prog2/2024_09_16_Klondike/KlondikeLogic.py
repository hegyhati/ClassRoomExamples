import FrenchDeck

NO_CARD = "░░"

class FoundationPile:
    def __init__(self, suit:FrenchDeck.Suit) -> None:
        self._suit = suit
        self._pile = FrenchDeck.Pile()
    
    def push_card(self, card:FrenchDeck.Card) -> None:
        if card.get_suit() != self._suit: raise ValueError("Different suit.")
        if self._pile.is_empty() and not card.is_ace(): raise ValueError("Foundation must start with Ace.")
        if not self._pile.is_empty() and card.get_rank() != self._pile.peek_top().get_rank() + 1: raise ValueError("Foundation must continue with the next rank.")
        self._pile.put_top(card)
    
    def pick_card(self) -> FrenchDeck.Card:
        if self._pile.is_empty(): raise ValueError("No cards in the foundation")
        else: return self._pile.pick_top()        
    
    def is_complete(self) -> bool:
        return self._pile.size() == FrenchDeck.RANK_COUNT
    
    def __str__(self) -> str:
        if self._pile.is_empty(): return NO_CARD
        else: return str(self._pile.peek_top())
        

class TableauPile:
    def __init__(self, size:int, source_deck:FrenchDeck.Pile) -> None:
        if size < 0 : raise ValueError("Tableau pile size must be non-negative.")
        if size > source_deck.size() : raise ValueError(f"Not enough cards in source deck for tableau pile of size {size}.")
        self._hidden  : FrenchDeck.Pile = FrenchDeck.Pile()
        self._visible : FrenchDeck.Pile = FrenchDeck.Pile()
        for _ in range(size):
            self._hidden.put_top(source_deck.pick_top())
    
    def __str__(self):
        return FrenchDeck.Card.BACK_DISPLAY * self._hidden.size() + str(self._visible)
    
    def reveal_top(self) -> None:
        if not self._visible.is_empty() : raise ValueError("The top card is already visible.")
        if self._hidden.is_empty() : raise ValueError("There are no cards in the tableau pile to reveal.")
        self._visible.put_top(self._hidden.pick_top())

    def pick_top(self) -> FrenchDeck.Card:
        if self._visible.is_empty() : raise ValueError("No revealed card to pick in tableau pile.")
        return self._visible.pick_top()
    
    def move_cards_to(self, other_tableau:"TableauPile") -> None:
        if self._visible.is_empty(): raise ValueError("Nothing to move.")
        if other_tableau.is_empty():
            if self._visible.peek_bottom().is_king():
                other_tableau._visible, self._visible = self._visible, other_tableau._visible
            else: raise ValueError("Only pile with King can be moved to empty tableau.")
        else:
            card = other_tableau.peek_top()
            rank = card.get_rank()-1
            if rank < self._visible.peek_top().get_rank() or rank > self._visible.peek_bottom().get_rank():
                raise ValueError(f"Card with rank {rank+1} not found.")
            same_color = FrenchDeck.Card.same_color(self._visible.peek_top(),card)
            same_parity = (card.get_rank() - self._visible.peek_top().get_rank()) % 2 == 0
            if same_color ^ same_parity: raise ValueError("Incompatible colors.")
            cards = []
            while True:
                cards.append(self.pick_top())
                if cards[-1].get_rank() == rank : break
            for card in reversed(cards):
                other_tableau.put(card)   
   
    def peek_top(self) -> FrenchDeck.Card:
        if self._visible.is_empty() : raise ValueError("No revealed card in tableau pile.")
        return self._visible.peek_top()

    def put(self, card:FrenchDeck.Card) -> None:
        if self._visible.is_empty():
            if not self._hidden.is_empty(): raise ValueError("Cannot put card on unrevealed card.")
            if not card.is_king(): raise ValueError("Only King can be moved to empty tableau pile.")
            self._visible.put_top(card)
        else:
            if FrenchDeck.Card.same_color(self._visible.peek_top(),card) : raise ValueError("Card must have different color.")
            if card.get_rank() + 1 != self._visible.peek_top().get_rank() : raise ValueError("Card must be one rank lower than top card.")
            self._visible.put_top(card)
            
    def is_empty(self) -> bool:
        return self._hidden.is_empty() and self._visible.is_empty()
 



class KlondikeGame:
    
    def __init__(self, tableau_count:int = 7, waste_pass_limit:int|None = None):
        if tableau_count < 1 : raise ValueError("At least one tableau is needed.")
        if tableau_count > 9 : raise ValueError("Not enough cars for tableaus.")
        
        self._waste_pass_limit = waste_pass_limit
        self._foundation = {
            suit: FoundationPile(suit)
            for suit in FrenchDeck.Suit
        }        
        self._hand = FrenchDeck.Pile.full_deck()
        self._waste = FrenchDeck.Pile()        
        self._tableau = [ TableauPile(size,self._hand) for size in range(1,tableau_count+1) ]
        
    def __str__(self) -> str:
        s = f"HAND: {self._hand.size()} × {FrenchDeck.Card.BACK_DISPLAY} → WASTE: "
        s += NO_CARD if self._waste.is_empty() else str(self._waste.peek_top())
        s += "\nFOUNDATION: "
        for suit in FrenchDeck.Suit:
            s += f"{suit.value}:{self._foundation[suit]}  "
        s += "\nTABLEAU:\n"
        for idx,tableau in enumerate(self._tableau):
            s += f" {idx+1} : {tableau}\n"
        return s
    
    def turn_hand(self) -> None:
        if self._hand.is_empty(): raise ValueError("Hand is empty.")
        self._waste.put_top(self._hand.pick_top())
    
    def __pass_waste(self) -> None:
        while not self._waste.is_empty():
            self._hand.put_top(self._waste.pick_top())
    
    def pass_waste(self) -> None:
        if not self._hand.is_empty(): raise ValueError("Hand not yet empty.")
        match self._waste_pass_limit: 
            case None : self.__pass_waste()
            case 0 : raise ValueError("No more waste passes remain.")
            case _ : 
                self.__pass_waste()
                self._waste_pass_limit -= 1
    
    def is_completed(self) -> bool:
        return all(foundation.is_complete() for foundation in self._foundation.values())
    
    def __check_tableau_idx(self, idx:int) -> None:
        if idx not in range(len(self._tableau)): raise ValueError(f"No such tableau pile: {idx+1}")
    
    def __check_waste(self) -> None:
        if self._waste.is_empty(): raise ValueError("Waste is empty")        
    
    def reveal_tableau(self, idx:int) -> None:
        self.__check_tableau_idx(idx)
        self._tableau[idx].reveal_top()
    
    def move_from_tableau_to_foundation(self, idx:int) -> None:
        self.__check_tableau_idx(idx)
        card = self._tableau[idx].peek_top()
        self._foundation[card.get_suit()].push_card(card)
        self._tableau[idx].pick_top()
    
    def move_from_waste_to_foundation(self)->None:
        self.__check_waste()
        card = self._waste.peek_top()
        self._foundation[card.get_suit()].push_card(card)
        self._waste.pick_top()
    
    # same logic for all three, generalize?
    def move_from_waste_to_tableau(self, idx:int)->None:
        self.__check_waste()
        self.__check_tableau_idx(idx)
        card = self._waste.peek_top()
        self._tableau[idx].put(card)
        self._waste.pick_top()
    
    # different logic, find issues with it
    def move_from_foundation_to_tableau(self, suit:FrenchDeck.Suit, idx:int) -> None:
        self.__check_tableau_idx(idx)
        card = self._foundation[suit].pick_card()
        try:
            self._tableau[idx].put(card)
        except ValueError as e:
            self._foundation[suit].push_card(card)            
            raise(e)
        
    def move_from_tableau_to_tableau(self, from_idx:int, to_idx:int) -> None:
        self.__check_tableau_idx(from_idx)
        self.__check_tableau_idx(to_idx)
        self._tableau[from_idx].move_cards_to(self._tableau[to_idx])
         
            
        
        
        
    
    
        
        
        
        
        
        
    
    

if __name__ == "__main__":
    game = KlondikeGame()
    print(game)
    for i in range(7):
        game.reveal_tableau(i)
        print(game)
        
            
            
        
        
        
        
    
            
        
    