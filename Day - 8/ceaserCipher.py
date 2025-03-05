# Caesar Cipher - Day 8 Project (with ASCII Art)

import string

# ASCII Art for the Caesar Cipher logo
logo = """           
 ██████╗ █████╗ ███████╗ █████╗ ██████╗      ██████╗██╗███████╗███████╗███████╗██████╗ 
██╔════╝██╔══██╗╚══███╔╝██╔══██╗██╔══██╗    ██╔════╝██║██╔════╝██╔════╝██╔════╝██╔══██╗
██║     ███████║  ███╔╝ ███████║██████╔╝    ██║     ██║█████╗  █████╗  █████╗  ██████╔╝
██║     ██╔══██║ ███╔╝  ██╔══██║██╔═══╝     ██║     ██║██╔══╝  ██╔══╝  ██╔══╝  ██╔══██╗
╚██████╗██║  ██║███████╗██║  ██║██║         ╚██████╗██║██║     ██║     ███████╗██║  ██║
 ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝          ╚═════╝╚═╝╚═╝     ╚═╝     ╚══════╝╚═╝  ╚═╝
"""

# Alphabet list (doubled to handle shifts beyond 'z')
alphabet = list(string.ascii_lowercase) * 2

def caesar_cipher(text, shift, direction):
    """Encrypts or decrypts a message using the Caesar Cipher."""
    result = ""
    shift = shift % 26  # Ensure shift stays within alphabet range

    if direction == "decode":
        shift *= -1  # Reverse shift for decryption

    for char in text:
        if char in alphabet:
            new_index = alphabet.index(char) + shift
            result += alphabet[new_index]
        else:
            result += char  # Keep punctuation & spaces unchanged

    return result

# Show ASCII art at the start
print(logo)
print("Welcome to the Caesar Cipher!")

# User Input Loop
while True:
    direction = input("Type 'encode' to encrypt, 'decode' to decrypt: ").lower()
    if direction not in ["encode", "decode"]:
        print("Invalid choice! Try again.")
        continue

    text = input("Enter your message: ").lower()
    shift = int(input("Enter the shift number: "))

    result = caesar_cipher(text, shift, direction)
    print(f"Here's the {direction}ed message: {result}")

    # Ask if the user wants to continue
    should_continue = input("Type 'yes' to go again, or 'no' to exit: ").lower()
    if should_continue != "yes":
        print("Goodbye!")
        break
