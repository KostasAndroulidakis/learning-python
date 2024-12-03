def digit_of_life(date):
    # Sum all digits in date string
    life_digit = sum(int(digit) for digit in date)
    # Calculate sum of digits until we get a single digit number
    while len(str(life_digit)) > 1:
        life_digit = sum(int(digit) for digit in str(life_digit))
    return life_digit

# Ensure valid 8-digit date format
while True:
    try:
        date = input("Enter your birthday: ")
        int(date)
        if int(date) <= 0:
            print("Invalid input: Birthday cannot be negative")
            continue
        if len(date) != 8:
            print("Invalid format: Enter 8 digits (YYYYMMDD)")
            continue          
        life_digit = digit_of_life(date)
        print(life_digit)
        break
    except ValueError:
        print("Invalid input: Enter digits only")