# ---------------- Day 9 Project: Secret Auction ----------------

import os

import os

def clear_screen():
    os.system("cls")  # Works in Windows command prompt (CMD)
    os.system("echo off")  # Ensures no unexpected outputs



# ASCII Art for the auction logo
logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                       .-------------.
                      /_______________\
'''

# Dictionary to store bids
bids = {}

def find_highest_bidder(bidding_record):
    """Finds the highest bidder and their bid amount."""
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}!")

# Display logo
print(logo)
print("Welcome to the secret auction program!")

# Auction loop
while True:
    name = input("Enter your name: ")
    bid = int(input("Enter your bid amount: $"))
    bids[name] = bid  # Store in dictionary

    more_bidders = input("Are there more bidders? Type 'yes' or 'no': ").lower()
    if more_bidders == "no":
        find_highest_bidder(bids)
        break
    else:
        clear_screen()