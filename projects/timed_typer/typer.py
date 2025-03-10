"""Plays a game where the user types random words within a time limit."""

import random
import time
import word_bank

def play_round(words, seconds):
    """Returns True if the user successfully completed the round."""
    # Run a stopwatch for the time it takes the user to respond.
    start = time.time()
    response = input("(" + str(seconds) + " seconds) " + words + "\n")
    stop = time.time()

    # Fail the round if a word is mispelled or if time runs out.
    within_time_limit = stop - start < seconds
    return response == words and within_time_limit

def pick_random_words(num_words, mode):
    """Returns a random phrase containing the given number of words.""" 
    words = ""
    for word in range(num_words):
        word = get_random_word(mode)
        words = words + " " + word

    return words.strip()

def get_random_word(mode):
    """Returns a random word with a word length based on the given mode."""
    if mode == "hard":
        words = word_bank.hard_words
    elif mode == "medium":
        words = word_bank.medium_words
    else:
        words = word_bank.easy_words

    return random.choice(words)

def get_level_parameters(level_number):
    """Difficulty levels"""
    if level_number == 1:  # Beginner
        mode = "easy"
        num_words = 2
        time_limit = 60
    elif level_number == 2:  # Intermediate
        mode = "medium"
        num_words = 2
        time_limit = 50
    elif level_number == 3:  # Hard
        mode = "medium"
        num_words = 3
        time_limit = 40
    elif level_number == 4:  # Expert
        mode = "hard"
        num_words = 1
        time_limit = 30
    elif level_number == 5:  # Master
        mode = "hard"
        num_words = 2
        time_limit = 40
    return mode, num_words, time_limit

def play_level(mode, num_words, time_limit):
    """Select difficulty level"""
    words = pick_random_words(num_words, mode)
    success = play_round(words, time_limit)
    return success

def play_multiple_rounds(level_number):
    """Play multiple rounds at the given level.
    Return True if player passes enough rounds."""
    mode, num_words, time_limit = get_level_parameters(level_number)
    
    rounds_played = 0
    successful_rounds = 0
    rounds_needed = 2  # Player needs to complete 2 rounds to pass
    
    while rounds_played < rounds_needed:
        # Generate new words for each round
        words = pick_random_words(num_words, mode)
        
        # Play the round
        success = play_round(words, time_limit)
        
        rounds_played += 1
        
        if success:
            successful_rounds += 1
            print(f"Round {rounds_played}: Success!({successful_rounds}/{rounds_needed} completed)")
        else:
            print(f"Round {rounds_played}: Failed. ({successful_rounds}/{rounds_needed} completed)")
    
    # Return whether player passed enough rounds
    return successful_rounds >= rounds_needed