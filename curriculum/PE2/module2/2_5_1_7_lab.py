def palindrome(text):
    # create a copy of original string to compare later
    original_text = text.replace(" ", "")
    # treat uppercase as lower
    original_text = original_text.lower()
    # reverse reverse_text
    reverse_text = original_text[::-1]
    # in case of empty
    if text == "":
        print("An empty message isn't a palindrome")
    # compare if reverse_text is a palindrome
    elif original_text == reverse_text:
        print("It's a palindrome")
    elif original_text != reverse_text:
        print("It's not a palindrome")

# ask user to enter a text
text = str(input("Enter text: "))
# call function to check if text is palindrome
palindrome(text)