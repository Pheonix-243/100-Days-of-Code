import random
import os

# Card deck (Ace is represented as 11 by default)
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

def deal_card():
    """Returns a random card from the deck."""
    return random.choice(cards)

def calculate_score(hand):
    """Calculates the score of a given hand."""
    if sum(hand) == 21 and len(hand) == 2:
        return 0  # 0 represents blackjack
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)

def compare(player_score, dealer_score):
    """Compares the final scores and returns the game result."""
    if player_score > 21:
        return "You went over. You lose! 😭"
    elif dealer_score > 21:
        return "Dealer went over. You win! 😃"
    elif player_score == dealer_score:
        return "It's a draw! 🙃"
    elif player_score == 0:
        return "Blackjack! You win! 😎"
    elif dealer_score == 0:
        return "Dealer has Blackjack! You lose! 😞"
    elif player_score > dealer_score:
        return "You win! 🎉"
    else:
        return "You lose! 😔"

def play_game():
    """Main function to run the Blackjack game."""
    os.system("cls" if os.name == "nt" else "clear")
    print("Welcome to Blackjack! 🃏")

    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]
    game_over = False

    while not game_over:
        player_score = calculate_score(player_hand)
        dealer_score = calculate_score(dealer_hand)

        print(f"Your cards: {player_hand}, current score: {player_score}")
        print(f"Dealer's first card: {dealer_hand[0]}")

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            game_over = True
        else:
            should_continue = input("Type 'y' to get another card, or 'n' to pass: ")
            if should_continue == "y":
                player_hand.append(deal_card())
            else:
                game_over = True

    while dealer_score != 0 and dealer_score < 17:
        dealer_hand.append(deal_card())
        dealer_score = calculate_score(dealer_hand)

    print(f"Your final hand: {player_hand}, final score: {player_score}")
    print(f"Dealer's final hand: {dealer_hand}, final score: {dealer_score}")
    print(compare(player_score, dealer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()
