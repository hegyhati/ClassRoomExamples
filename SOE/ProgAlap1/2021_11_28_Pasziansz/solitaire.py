from card import *

def initialize_game(pile_count:int=7) -> dict:
    stock = get_shuffled_card_deck()
    piles = [
        {
            'deck': get_empty_deck(),
            'visible': 1
        }
        for _ in range(pile_count)
    ]
    for idx, pile in enumerate(piles):
        for _ in range(idx+1):
            push_card_to_deck(pop_top_card(stock), pile['deck'])

    return {
        'stock': stock,
        'stock_used': get_empty_deck(),
        'piles': piles,
        'foundations': {ctype: get_empty_deck() for ctype in card_type}
    }


def print_game_state(gamestate: dict) -> None:
    print('Stock: ', end='')
    print_deck(gamestate['stock'])
    print()
    print('Piles:')
    for idx, pile in enumerate(gamestate['piles']):
        print(f' {idx+1}: ', end='')
        print_deck(pile['deck'], pile['visible'])
        print()
    print('Foundations:')
    for type, foundation in gamestate['foundations'].items():
        print(f' {type}: ', end='')
        print_deck(foundation, visible=len(foundation))
        print()


def skip_stock(gamestate: dict) -> None:
    push_card_to_deck(
        card=pop_top_card(gamestate['stock']),
        deck=gamestate['stock_used'],
        top=False
    )
    if is_empty(gamestate['stock']):
        gamestate['stock'], gamestate['stock_used'] = gamestate['stock_used'], gamestate['stock']


def can_push_to_pile(card:Card, pile:dict):
    if is_empty(pile['deck']):
        return is_largest(card)
    elif pile['visible'] == 0:
        return False
    pile_top_card=top_card(pile['deck'])
    return not is_same_color(card,pile_top_card) and has_one_greater_value(pile_top_card,card)

def push_stock_to_pile(gamestate: dict, pile_idx: int):
    if is_empty(gamestate['stock']):
        print(f"A stock ures, nem lehet belole pakolni.")
        return
    if not can_push_to_pile(top_card(gamestate["stock"]),gamestate['piles'][pile_idx]):
        print(f"Nem lehet a {to_string(top_card(gamestate['stock']))} -ot a {pile_idx+1}. pile-ra pakolni.")
        return 
    push_card_to_deck(
        card=pop_top_card(gamestate['stock']),
        deck=gamestate['piles'][pile_idx]['deck']
    )
    gamestate['piles'][pile_idx]['visible'] += 1


def can_push_to_foundation(gamestate:dict, card:Card) -> bool:
    foundation_deck = gamestate['foundations'][get_type(card)]
    if is_empty(foundation_deck):
        return is_smallest(card)
    return has_one_greater_value(card,top_card(foundation_deck))   


def push_pile_to_foundation(gamestate: dict, pile_idx: int):
    if is_empty(gamestate['piles'][pile_idx]['deck']):
        print(f"A {pile_idx+1}. pile ures, nem lehet rola felpakolni.")
        return
    if gamestate['piles'][pile_idx]['visible'] == 0:
        print(f"A {pile_idx+1}. pile-on nincs felforditva a legfelso lap.")
        return
    if not can_push_to_foundation(gamestate, top_card(gamestate['piles'][pile_idx]['deck'])):
        print(f"{to_string(top_card(gamestate['piles'][pile_idx]['deck']))} nem felpakolhato.")
        return 
    pile_top_card = pop_top_card(gamestate['piles'][pile_idx]['deck'])
    gamestate['piles'][pile_idx]['visible']-=1
    push_card_to_deck(
        card = pile_top_card,
        deck = gamestate['foundations'][get_type(pile_top_card)]
    )


def push_stock_to_foundation(gamestate: dict):
    if is_empty(gamestate['stock']):
        print(f"A stock ures, nem lehet rola felpakolni.")
        return
    if not can_push_to_foundation(gamestate, top_card(gamestate['stock'])):
        print(f"{to_string(top_card(gamestate['stock']))} nem felpakolhato.")
        return 
    stock_top_card = pop_top_card(gamestate['stock'])
    push_card_to_deck(
        card = stock_top_card,
        deck = gamestate['foundations'][get_type(stock_top_card)]
    )

def reveal_pile_top_card(gamestate:dict, pile_idx:int):
    if gamestate['piles'][pile_idx]['visible'] > 0:
        print(f"A {pile_idx+1}. pile legfelso lapja nem leforditott.")
        return
    if is_empty(gamestate['piles'][pile_idx]['deck']):
        print(f"A {pile_idx+1}. pile ures.")
        return
    gamestate['piles'][pile_idx]['visible']+=1

def move_cards_between_piles(gamesate:dict, from_pile_idx:int, card_count: int, to_pile_idx:int):
    if gamesate['piles'][from_pile_idx]['visible'] < card_count:
        print(f"A {from_pile_idx+1}. pile-on nincs eleg felforditott kartya.")
        return
    if not can_push_to_pile(top_card(gamesate['piles'][from_pile_idx]['deck'], card_count), gamesate['piles'][to_pile_idx]):
        print(f"Nem megfelelok a kartyak az atpakolashoz ({to_string(top_card(gamesate['piles'][from_pile_idx]['deck'], card_count))} nem rakhato a {to_pile_idx+1}. pile-ra.")
        return
    hand = []
    for _ in range(card_count):
        push_card_to_deck(
            card=pop_top_card(gamesate['piles'][from_pile_idx]['deck']),
            deck= hand
        )
        gamesate['piles'][from_pile_idx]['visible']-=1
    
    for _ in range(card_count):
        push_card_to_deck(
            card=pop_top_card(hand),
            deck=gamesate['piles'][to_pile_idx]['deck']
        )
        gamesate['piles'][to_pile_idx]['visible']+=1
    

def is_won(gamestate:dict)->bool:
    if not is_empty(gamestate['stock']):
        return False
    if not is_empty(gamestate['stock_used']):
        return False
    for pile in gamestate['piles']:
        if not is_empty(pile['deck']):
            return False
    return True


gs = initialize_game(4)

while not is_won(gs):
    print_game_state(gs)
    command = input('Mit csinalsz? ')
    if command == 'S':
        skip_stock(gs)
    elif command[0] == 'P':
        push_stock_to_pile(gs, int(command[1:])-1)
    elif command[0] == 'F':
        if len(command)==1:
            push_stock_to_foundation(gs)
        else:
            push_pile_to_foundation(gs, int(command[1:])-1)
    elif command[0] == "T":
        reveal_pile_top_card(gs,int(command[1:])-1)
    elif command[0] == "M":
        (from_pile, count, to_pile) = ( int(x) for x in command[1:].split(","))
        move_cards_between_piles(gs,from_pile-1,count,to_pile-1)

print("Grat.")