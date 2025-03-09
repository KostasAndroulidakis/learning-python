# Define LED display patterns for digits 0-9
LED_NUMBERS = (
    # 0
    ("# # #",
     "#   #",
     "#   #",
     "#   #",
     "# # #"),
    # 1     
    ("#",
     "#",
     "#",
     "#",
     "#"),
    # 2
    ("# # #",
     "    #",
     "# # #",
     "#    ",
     "# # #"),
    # 3
    ("# # #",
     "    #",
     "# # #",
     "    #",
     "# # #"),
    # 4
    ("#   #",
     "#   #",
     "# # #",
     "    #",
     "    #"),
    # 5
    ("# # #",
     "#    ",
     "# # #",
     "    #",
     "# # #"),
    # 6
    ("# # #",
     "#    ",
     "# # #",
     "#   #",
     "# # #"),
    # 7
    ("# # #",
     "    #",
     "    #",
     "    #",
     "    #"),
    # 8
    ("# # #",
     "#   #",
     "# # #",
     "#   #",
     "# # #"),
    # 9
    ("# # #",
     "#   #",
     "# # #",
     "    #",
     "# # #"),
)

# Create LED pattern from input number
def led_pattern(number_string):
    led_number = []
    for line in range(5):
        current_line = ""
        for digit in number_string:
            current_line += f"{LED_NUMBERS[int(digit)][line]}  "
        led_number.append(current_line)
    return(led_number)

# Display LED pattern on screen
def led_display(pattern):
    for line in pattern:
        print(line)

# Validate and process user input, ensuring non-negative integer
while True:
    try:
        user_input = input("Enter a non-negative integer number: ")
        number = int(user_input)
        if number >= 0:
            pattern = led_pattern(number_string = str(number))
            led_display(pattern)
            break
        else:
            print(f'SYSTEM ERROR: The number "{user_input}" is negative! Please enter a non-negative number.')
    except ValueError:
        print(f'SYSTEM ERROR: "{user_input}" is not a number! Please enter a valid integer number.')