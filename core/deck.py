import random

def creat_card(rank:str,suite:str) -> dict:
    card = {} 
    card['rank'] = rank
    card['suite'] = suite
    return card 

def build_standard_deck() -> list[dict]:
    ranks = [str(i) for i in range(2,11)] + [ 'J','Q','K','A'] 
    suits = ['H','C','D','S']
    cards = [] 
    for i in range(4):
        for j in range(13):
            cards.append(creat_card(ranks[j],suits[i]))
    return cards

def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:
    for _ in range(swaps):
        is_j_valid = False
        
        while not is_j_valid:
            
            indexes = random.sample(range(0,len(deck)-1),2)
            i = indexes[0]
            j = indexes[1]
            
            card_i = deck[i]
            card_j = deck[j]
            
            suite = card_i['suite']
            
            match suite:
                case 'H':
                    if j % 5 != 0:
                        continue
                case 'C':
                    if j % 3 != 0:
                        continue
                case 'D':
                    if j % 2 != 0:
                        continue
                case 'S':
                    if j % 7 != 0:
                        continue
            is_j_valid = True
        
        temp = deck[i]
        deck[i] = deck[j]
        deck[j] = temp
        
    # print(f'{i} , {j} {suite} {is_j_valid}')
    return deck

shuffled_deck = shuffle_by_suit(deck=build_standard_deck())
       
        
        
