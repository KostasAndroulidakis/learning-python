# checks whether, the entered texts are anagrams and prints the result
def anagrams(word1, word2):
    # remove spaces from words
    word1 = word1.replace(" ", "")
    word2 = word2.replace(" ", "")
    # convert to lowercase to ignore letter casing
    word1 = word1.lower()
    word2 = word2.lower()
    # create empty lists to store characters
    word1list = []
    word2list = []
    # add words to lists
    for char in word1:
        word1list.append(char)
    for char in word2:
        word2list.append(char)
    # sort list alphabetically
    word1list.sort()
    word2list.sort()
    # check for anagram
    if word1list == word2list:
        print("Anagrams")
    else:
        print("Not anagrams")

# ask user to enter 2 words
word1 = input("Enter the 1st word: ")
word2 = input("Enter the 2nd word: ")

# call function to check if text are anagrams
anagrams(word1, word2)