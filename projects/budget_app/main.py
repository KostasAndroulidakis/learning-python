from budget import Category, create_spend_chart

# Create budget categories
food = Category("Food")
clothing = Category("Clothing")
entertainment = Category("Entertainment")
auto = Category("Auto")

# Add money to categories
food.deposit(1000, "initial deposit")
clothing.deposit(500, "initial deposit")
entertainment.deposit(300, "initial deposit")
auto.deposit(800, "initial deposit")

# Make withdrawals
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
clothing.withdraw(100, "winter jacket")
entertainment.withdraw(33.40, "cinema")
entertainment.withdraw(17.28, "video game")
auto.withdraw(120, "insurance")
auto.withdraw(99.99, "maintenance")

# Transfer between categories
food.transfer(50, clothing)

# Print each category
print(food)
print("\n")
print(clothing)
print("\n")
print(entertainment)
print("\n")
print(auto)
print("\n")

# Create and print spending chart
chart = create_spend_chart([food, clothing, entertainment, auto])
print(chart)