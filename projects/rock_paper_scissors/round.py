import random

"""Supports a round of rock, paper, scissors between a user and a computer."""

def make_user_choice():
    """Returns the user's choice of rock, paper, or scissors."""
    while True:
        choice = input("Choose one: rock, paper, scissors? ")
        choice = choice.lower().strip()
        if choice in ["rock", "paper", "scissors"]:
            return choice
        else:
            print("Invalide choice. Please enter rock, paper, or scissors.")

def make_computer_choice():
    """Returns the computer's random choice of rock, paper, or scissors."""
    choice = random.randint(1,3)
    if choice == 1:
        choice = "rock"
    elif choice == 2:
        choice = "paper"
    elif choice == 3:
        choice = "scissors"
    return choice

def wins_matchup(choice, opponent_choice):
    """Returns True if the first player's choice wins over their opponent.
    Choices can be rock, paper, or scissors. Assumes the choices are different.
    """
    if choice == "rock" and opponent_choice == "scissors":
        return True
    elif choice == "scissors" and opponent_choice == "paper":
        return True
    elif choice == "paper" and opponent_choice == "rock":
        return True
    else:
        return False

def format_score(user_score, computer_score):
    """Returns a formatted version of the players's current scores."""
    user = "user (" + str(user_score) + ")"
    computer = "computer (" + str(computer_score) + ")"
    return user + " vs. " + computer
