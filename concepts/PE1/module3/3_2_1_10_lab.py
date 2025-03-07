# Prompt the user to enter a word
# and assign it to the user_word variable.
user_word = input("Enter a word: ")

# Convert word to upper letters
user_word = user_word.upper()

for letter in user_word:
    if letter in ['A', 'E', 'I', 'O', 'U']:
        continue
    else:
        print(letter)