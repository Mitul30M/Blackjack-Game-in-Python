import random
import os

def clear_console():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Unix-based systems (Linux, macOS)
        os.system('clear')
clear_console()

game = {
    "dealer": {
        "cards": [],
        "score": 0,
        "isWinner": False,
        "chips_bet": 0,
        "chips_balance": 1500
    },
    "user": {
        "cards": [],
        "score": 0,
        "isWinner": False,
        "chips_bet": 0,
        "chips_balance": 1500
    },
    "is_game_over": False,
}
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def count_elements(arr):
    counts = {}
    for element in arr:
        if element in counts:
            counts[element] += 1
        else:
            counts[element] = 1
    return counts

def adjust_for_ace(player):
    while player["score"] > 21 and 11 in player["cards"]:
        ace_index = player["cards"].index(11)
        player["cards"][ace_index] = 1
        player["score"] = sum(player["cards"])

def check_blackjack(player):
    return player["score"] == 21

def check_bust(player):
    return player["score"] > 21

def draw_card(player):
    while True:
        new_card = random.choice(cards)
        player["cards"].append(new_card)
        hand_info = count_elements(player['cards'])

        # Check if a card (except 10) appears more than 4 times
        if new_card != 10 and hand_info[new_card] > 4:
            player["cards"].pop()
        else:
            player["score"] = sum(player["cards"])
            adjust_for_ace(player)
            break

def compare_scores():
    user_score = game["user"]["score"]
    dealer_score = game["dealer"]["score"]

    if user_score > dealer_score:
        print(f"{game['user']['cards']}\nYou WIN the round!\n")
        game['user']['chips_balance'] += game['user']['chips_bet'] * 2
        game['user']['isWinner'] = True
    elif user_score < dealer_score:
        print(f"{game['dealer']['cards']}\nDEALER wins the round! You LOSE\n")
        game['dealer']['chips_balance'] += game['dealer']['chips_bet'] * 2
        game['dealer']['isWinner'] = True
    else:
        print(f"{game['dealer']['cards']}\n{game['user']['cards']}\nThe round ends in a DRAW!")
        game['user']['chips_balance'] += game['user']['chips_bet']
        game['dealer']['chips_balance'] += game['dealer']['chips_bet']

    game['user']['chips_bet'] = 0
    game['dealer']['chips_bet'] = 0

    print(f"\nCHIPS BALANCE: {game['user']['chips_balance']}")

def play_round():
    while True:
        clear_console()
        print("\n♠️♥️♣️♦️ BLACKJACK by mitul30m ♠️♥️♣️♦️\n")
        game["dealer"]["cards"] = []
        game["dealer"]["score"] = 0
        game["dealer"]["isWinner"] = False

        game["user"]["cards"] = []
        game["user"]["score"] = 0
        game["user"]["isWinner"] = False

        print("\n\n♠️♥️♣️♦️ New Round ♠️♥️♣️♦️\n")

        print(f"CHIP BALANCE = {game['user']['chips_balance']}")

        game['user']['chips_bet'] = int(input(f"Enter your BET (CHIPS BALANCE: {game['user']['chips_balance']}) : "))
        game['dealer']['chips_bet'] = game['user']['chips_bet']
        game['user']['chips_balance'] -= game['user']['chips_bet']
        game['dealer']['chips_balance'] -= game['dealer']['chips_bet']

        random.shuffle(cards)
        print("Shuffling cards...♠️♥️♣️♦️")

        for _ in range(2):
            draw_card(game["user"])
            draw_card(game["dealer"])

        print(f"Dealer has dealt you a hand of 2 cards: {game['user']['cards']}\n")

        if check_blackjack(game["user"]):
            print(f"BLACKJACK {game['user']['cards']}\nYou WIN the round!\n")
            game['user']['chips_balance'] += game['user']['chips_bet'] * 2
            game['user']['isWinner'] = True
            print(f"\nCHIPS BALANCE: {game['user']['chips_balance']}")
        elif check_blackjack(game["dealer"]):
            print(f"BLACKJACK {game['dealer']['cards']}\nDEALER wins the round! You LOSE!\n")
            game['dealer']['chips_balance'] += game['dealer']['chips_bet'] * 2
            game['dealer']['isWinner'] = True
            print(f"\nCHIPS BALANCE: {game['user']['chips_balance']}")
        else:
            while True:
                print(f"\nDealer's FIRST CARD IS {game['dealer']['cards'][0]}")
                user_choice = input(f"\nYour Hand: {game['user']['cards']} (hand total: {game['user']['score']}), \nDo you wish to HIT or STAND?\n").strip().lower()

                if user_choice == 'hit':
                    draw_card(game["user"])
                    print(f"\nYour Hand: {game['user']['cards']} (hand total: {game['user']['score']})")
                    if check_bust(game["user"]):
                        print(f"\n\n{game['dealer']['cards']}\nDEALER wins the round!,\n{game['user']['cards']} You LOSE\n")
                        game['dealer']['chips_balance'] += game['dealer']['chips_bet']
                        game['dealer']['isWinner'] = True
                        print(f"\nCHIPS BALANCE: {game['user']['chips_balance']}")
                        break
                else:
                    while game["dealer"]["score"] < 17:
                        draw_card(game["dealer"])

                    print(f"\n\nDealer's Hand: {game['dealer']['cards']} (hand total: {game['dealer']['score']})")
                    print(f"\nYour Hand: {game['user']['cards']} (hand total: {game['user']['score']})\n")

                    if check_bust(game["dealer"]):
                        print(f"{game['user']['cards']}\nYou WIN the round!\n")
                        game['user']['chips_balance'] += game['user']['chips_bet'] * 2
                        game['user']['isWinner'] = True
                        print(f"\nCHIPS BALANCE: {game['user']['chips_balance']}")
                    else:
                        compare_scores()
                    break

        if game['user']['chips_balance'] <= 0:
            print("You are out of chips! Dealer wins the game of BLACKJACK.")
            break

        if game['dealer']['chips_balance'] <= 0:
            print("Dealer is out of chips! You win the game of BLACKJACK.")
            break

        play_again = input("Do you want to play another round? (yes/no): ").strip().lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    play_round()
