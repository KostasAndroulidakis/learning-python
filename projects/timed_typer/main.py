import typer

print("Type the words and hit enter within the time limit!")

current_level = 1
while current_level <= 5:
    print(f"Level {current_level}")
    # Get difficulty info to display to player
    if current_level == 1:
        difficulty = "Beginner"
    elif current_level == 2:
        difficulty = "Intermediate"
    elif current_level == 3:
        difficulty = "Hard"
    elif current_level == 4:
        difficulty = "Expert"
    elif current_level == 5:
        difficulty = "Master"
    print(f"Difficulty: {difficulty}")
    
    # Call your level function and check result
    success = typer.play_multiple_rounds(current_level)
    
    if success:
        current_level += 1
    else:
        print("Game over! Try again.")
        break

# completion
if current_level > 5:
    print("You mastered the game! Thanks for playing.")
