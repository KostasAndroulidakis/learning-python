# Prepare an empty string
word_without_vowels = ""

# Prompt the user to enter a word
user_word = input("Enter a word: ")

# Convert word to upper letters
user_word = user_word.upper()

for letter in user_word:
    if letter in ['A', 'E', 'I', 'O', 'U']:
        continue
    else:
        word_without_vowels += letter
        
# Print the word assigned to word_without_vowels.
print(word_without_vowels)