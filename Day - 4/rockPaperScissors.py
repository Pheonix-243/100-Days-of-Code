import random

print("Welcome to Rock, Paper, Scissors!")
print("""
      ROCK          PAPER         SCISSORS
    _______        _______       _______
---'   ____)    ---'   ____)    ---'   ____)____
      (_____)         (_____)         (______)
      (_____)         (_____)         (______)
      (____)         (______)        (______)
---.__(___)      ---.__(___)       ---.__(___)
""")

choices = ["rock", "paper", "scissors"]

ascii_art = {
    "rock": """
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """,
    "paper": """
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    """,
    "scissors": """
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """
}

player_choice = int(input("Choose: 1. Rock, 2. Paper, or 3. Scissors: "))

# Validate input
if player_choice not in [1, 2, 3]:
    print("Invalid choice! Please choose 1, 2, or 3.")
else:
    # Generate computer choice (1 to 3)
    computer_choice = random.randint(1, 3)

    player_move = choices[player_choice - 1]
    computer_move = choices[computer_choice - 1]

    print("\nYou chose:", player_move)
    print(ascii_art[player_move])

    print("Computer chose:", computer_move)
    print(ascii_art[computer_move])

    # Determine the winner
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == 1 and computer_choice == 3) or \
         (player_choice == 2 and computer_choice == 1) or \
         (player_choice == 3 and computer_choice == 2):
        print("You win! 🎉")
    else:
        print("You lose! 😢")
