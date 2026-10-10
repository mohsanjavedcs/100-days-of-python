import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def deal_cards():
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(player_score, dealer_score):
    if dealer_score == player_score:
        return "it's a draw!"
    elif dealer_score == 0:
        return "The dealer has a Blackjack, You Lose."
    elif player_score == 0:
        return "You have a Blackjack, You Win!"
    elif player_score > 21:
        return "You went over, You Lose."
    elif dealer_score > 21:
        return "Dealer went over, You Win!"
    elif player_score > dealer_score:
        return "You Win!"
    else:
        return "You Lose."

def play_game():
    player_cards = []
    dealer_cards = []
    is_game_over = False

    for _ in range(2):
        player_cards.append(deal_cards())
        dealer_cards.append(deal_cards())

    while not is_game_over:
        player_score = calculate_score(player_cards)
        dealer_score = calculate_score(dealer_cards)

        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Dealer's first card: {dealer_cards[0]}, current score: {dealer_score}")

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            is_game_over = True
        else:
            choice = input("Type 'y' to get another card, type 'n' to pass: ")
            if choice == "y":
                player_cards.append(deal_cards())
            else:
                is_game_over = True

    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_cards())
        dealer_score = calculate_score(dealer_cards)

    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")
    print(compare(player_score, dealer_score))

while input("Do you want to play BlackJack? Type 'y' or 'n': ").lower() == "y":
    clear_terminal()
    play_game()