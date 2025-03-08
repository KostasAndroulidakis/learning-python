# ask the user to enter the unencrypted one-line message
text = input("Enter your message: ")

# Validate shift value between 1-25
def validate_shift_value():
    # Loop until user enters an integer between 1-25
    while True:
        # Get shift value
        shift_value = input("Enter shift value (1-25): ")
        # remove leading/trailing spaces from input
        shift_value = shift_value.strip()
        # if number is valid:
        if shift_value.isdigit():
            # convert string to int
            shift_value = int(shift_value)
            if shift_value < 1 or shift_value > 25:
                print(f'ERROR: The "{shift_value}" is not between 1 and 25! Please enter a valid shift value.')
            else:
                return int(shift_value)
        else: 
            print(f'ERROR: The "{shift_value}" is not a number! Please enter a valid shift value between 1 and 25.')

shift_value = validate_shift_value()

# Convert character to ASCII, shift it and convert back to character
def caesar_cipher(text, shift_number):
    cipher = ''
    for char in text:
        if char.isalpha():
            # Use modulo 26 to wrap around the alphabet
            ALPHABET_SIZE = 26
            # 65 is ASCII for 'A', 97 is ASCII for 'a'
            if char.isupper():
                char = chr((((ord(char) - 65) + shift_number)%ALPHABET_SIZE)+65)
            else:
                char = chr((((ord(char) - 97) + shift_number)%ALPHABET_SIZE)+97)
        cipher = cipher + char
    return cipher

cipher = caesar_cipher(text, shift_value)
print(cipher)