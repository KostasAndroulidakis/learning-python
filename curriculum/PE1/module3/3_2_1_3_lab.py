secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

user_number = int(input("Enter an integer number: "))

while user_number != secret_number:
    print("Ha ha! You're stuck in my loop!")
    user_number = int(input("Try again! Enter an integer number: "))

print('"Well done, muggle! You are free now."')