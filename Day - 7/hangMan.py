import random

# Word list for the Hangman game
word_list = ["aardvark", "baboon", "camel"]

# Randomly choose a word from the word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Initialize variables
end_of_game = False
lives = 6

# Create blanks
display = ["_"] * word_length

# Hangman ASCII art stages (starts empty and adds parts)
stages = [
    '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    '''
]

# Game loop
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Check guessed letter
    if guess in display:
        print("You've already guessed this letter.")
        continue  # Prevent losing a life for repeated guesses

    correct_guess = False
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            correct_guess = True

    # If guess is not in the chosen_word
    if not correct_guess:
        lives -= 1
        print(f"Wrong guess! You have {lives} lives left.")
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The word was: {chosen_word}")

    # Join all the elements in the list and turn it into a String
    print(f"{' '.join(display)}")

    # Check if user has got all letters
    if "_" not in display:
        end_of_game = True
        print("You win!")

    # Print the correct hangman stage
    print(stages[6 - lives])  # Flipped to match increasing mistakes
