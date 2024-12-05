def find_a_word():
    # Ask user to enter 2 words
    word1 = input("Enter the first word: ")
    word2 = input("Enter the second word: ")
    pos = 0
    # Check if character in second word starting from pos
    for char in word1:
        # Update pos to ensure characters are found in sequence
        pos = word2.find(char, pos)
        if pos == -1:
            print("No")
            return
    print("Yes")
    return

find_a_word()