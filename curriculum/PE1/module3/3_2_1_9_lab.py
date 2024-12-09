secret_word = "chupacabra"
user_word = input("Enter a word: ")

while True:
    if user_word == secret_word:
        break
    user_word = input("Wrong! Try again!\nEnter a word: ")

print("You've successfully left the loop.")