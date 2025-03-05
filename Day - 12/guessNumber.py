import random

logo = """
 _   _                 _                 _               
| \ | |               | |               (_)              
|  \| | ___  _ __ ___ | |__   ___  ___   _  ___  _ __    
| . ` |/ _ \| '_ ` _ \| '_ \ / _ \/ __| | |/ _ \| '_ \   
| |\  | (_) | | | | | | |_) | (_) \__ \ | | (_) | | | |  
\_| \_/\___/|_| |_| |_|_.__/ \___/|___/ |_|\___/|_| |_|  

"""


def guess_number():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    number = random.randint(1, 100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    attempts = 10 if difficulty == "easy" else 5

    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if guess == number:
            print(f"You got it! The answer was {number}.")
            return
        elif guess < number:
            print("Too low.")
        else:
            print("Too high.")

        attempts -= 1
        if attempts == 0:
            print(f"You've run out of guesses. The number was {number}.")
            return
        else:
            print("Guess again.")


# Start the game
guess_number()
