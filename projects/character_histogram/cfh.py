# 4.3.1.15 LAB: Character frequency histogram

try:
    filename = input("Enter the file name: ")
    
    with open(filename, 'r') as file:
        content = file.read()
    
    letter_counts = {}
    
    for char in content:
        if char.isalpha():  # Check if the character is a letter
            char = char.lower()  # Convert to lowercase for uniformity
            if char in letter_counts:
                letter_counts[char] += 1  # Increment count for existing letter
            else:
                letter_counts[char] = 1  # Initialize count for new letter
    
    for char in sorted(letter_counts.keys()):
        print(f"{char} -> {letter_counts[char]}")
        
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except PermissionError:
    print(f"Error: You don't have permission to read '{filename}'.")
except Exception as e:
    print(f"An error occurred: {e}")