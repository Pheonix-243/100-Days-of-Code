import random
from data import game_data

logo = r"""
  _    _ _       _                _           
 | |  | (_)     | |              | |          
 | |__| |_  __ _| |__   ___ _ __ | |_ ___     
 |  __  | |/ _` | '_ \ / _ \ '_ \| __/ _ \    
 | |  | | | (_| | | | |  __/ | | | || (_) |   
 |_|  |_|_|\__, |_| |_|\___|_| |_|\__\___/    
            __/ |                              
           |___/                               
"""


def get_random_account():
    """Get a random account from the game data"""
    return random.choice(game_data)


def format_account(account):
    """Format the account data into a printable string"""
    return f"{account['name']}, a {account['description']}, from {account['country']}"


def check_answer(guess, a_followers, b_followers):
    """Checks if the user guessed correctly"""
    return (guess == 'a' and a_followers > b_followers) or (guess == 'b' and b_followers > a_followers)


def game():
    print(logo)
    score = 0
    should_continue = True
    account_b = get_random_account()

    while should_continue:
        account_a = account_b
        account_b = get_random_account()
        while account_a == account_b:
            account_b = get_random_account()

        print(f"Compare A: {format_account(account_a)}")
        print("VS")
        print(f"Against B: {format_account(account_b)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_followers = account_a["follower_count"]
        b_followers = account_b["follower_count"]

        if check_answer(guess, a_followers, b_followers):
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            should_continue = False


game()
