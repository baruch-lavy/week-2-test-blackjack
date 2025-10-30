from core.deck import shuffled_deck
from core.game_logic import run_full_game

if __name__ == "__main__":
    deck = shuffled_deck
    player = {"hand": [ ] }
    dealer = {"hand": [ ] }

    run_full_game(deck,player,dealer)