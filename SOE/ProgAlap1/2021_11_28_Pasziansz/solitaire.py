from card import *


def initialize_game() -> dict:
    stock = get_shuffled_card_deck()
    piles = [
        {
            'deck': get_empty_deck(),
            'visible': 1
        }
        for _ in range(7)
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
    # todo empty pile and K -> True
    pile_top_card=top_card(pile['deck'])
    return not is_same_color(card,pile_top_card) and has_one_greater_value(pile_top_card,card)

def push_stock_to_pile(gamestate: dict, pile_idx: int):
    if not can_push_to_pile(top_card(gamestate["stock"]),gamestate['piles'][pile_idx]):
        print(f"Nem lehet a {to_string(top_card(gamestate['stock']))} -ot a {pile_idx+1}. pile-ra pakolni.")
        return 
    push_card_to_deck(
        card=pop_top_card(gamestate['stock']),
        deck=gamestate['piles'][pile_idx]['deck']
    )
    gamestate['piles'][pile_idx]['visible'] += 1


gs = initialize_game()

while True:
    print_game_state(gs)
    command = input('Mit csinalsz? ')
    if command == 'S':
        skip_stock(gs)
    elif command[0] == 'P':
        push_stock_to_pile(gs, int(command[1:])-1)
