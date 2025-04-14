# 4.3.1.16 LAB: Sorted character frequency histogram

filename = input("Enter the file name: ")
with open(filename, 'r') as file:
    content = file.read()

char_frequency = {}
for char in content:
    if char.isalpha():
        char = char.lower()
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1

# Short the dictionary by frequency
sorted_frequency = sorted(char_frequency.items(), key=lambda item: item[1], reverse=True)
for char, frequency in sorted_frequency:
    print(f"{char} -> {frequency}")

# Save results to a file
output_filename = filename + ".hist"
with open(output_filename, 'w') as output_file:
    for char, frequency in sorted_frequency:
        output_file.write(f"{char} -> {frequency}\n")