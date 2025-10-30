from core.deck import shuffled_deck
from core.player_io import ask_player_action


def calculate_hand_value(hand: list[dict]) -> int:
    hand_value = 0
    for card in hand:
        try:
            hand_value += int(card['rank'])
            
        except ValueError:
            rank = card['rank']
            ranks_10 = ['J','Q','K']
            if rank in ranks_10:
                hand_value += 10
            else:
                hand_value += 1
    return hand_value

def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
    
    for i in range(4):
        if i <= 1:
            player['hand'].append(deck.pop(i))
        else:
            dealer['hand'].append(deck.pop(i))
    print(f'player hand value is {calculate_hand_value(player['hand'])}')
    print(f'dealer hand value is {calculate_hand_value(dealer['hand'])}')

def dealer_play(deck: list[dict], dealer: dict) -> bool:
    is_playing = True
    
    while is_playing:
        dealer['hand'].append(deck.pop(0))
        hand_value = calculate_hand_value(dealer['hand'])
        if hand_value >= 17:
            if hand_value > 17 and hand_value > 21:
                is_playing = False
                return False
            elif hand_value >= 17 or hand_value <= 21:
                is_playing = False
                print(f'dealer is o.k {hand_value}')
                return True
 
def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    deal_two_each(deck,player,dealer)
    
    is_palyer_turn = True
    player_hand = player['hand']
    while is_palyer_turn:
        if calculate_hand_value(player_hand) <= 21:
            print(f'your current hand value is {calculate_hand_value(player_hand)}')
        user_action = ask_player_action()
        
        if user_action == 'H':
            player_hand.append(deck.pop(0))
            player_hand_value = calculate_hand_value(player_hand)
            if player_hand_value > 21:
                is_palyer_turn = False
                print(f'you have lost your hand value is {player_hand_value}')
        elif user_action == 'S':
            is_palyer_turn = False
            dealer_score = dealer_play(deck,dealer)
            if dealer_score == False:
                print(f'dealer lost {calculate_hand_value(dealer['hand'])}')
            else:
                player_hand_value = calculate_hand_value(player_hand)
                dealer_hand_value = calculate_hand_value(dealer['hand'])
                
                if player_hand_value > dealer_hand_value:
                    print(f'player won {player_hand_value}')
                elif player_hand_value < dealer_hand_value:
                    print(f'dealer won {dealer_hand_value}')
                else:
                    print('draw')
                
            
            
             
