class Category:
    """Category class"""
    def __init__(self, category):
        self.ledger = []
        self.category = category
    
    def deposit(self, amount, description=''):
        if description is None:
            description = ''
        self.ledger.append({
                'amount': amount,
                'description': description
                })
    
    def check_funds(self, amount):
        balance = 0
        for entry in self.ledger:
            balance += entry['amount']
        return amount <= balance

    def withdraw(self, amount, description=''):
        # First check if there are enough funds
        if self.check_funds(amount):
            # If we have enough funds add a negative entry to the ledger
            self.ledger.append({
                'amount': -amount,  # Store as negative
                'description': description
                })
            return True  # Withdrawal succeeded
        else:
            # If not enough funds, don't modify ledger
            return False  # Withdrawal failed

    def get_balance(self):
        balance = 0
        for entry in self.ledger:
            balance += entry['amount']
        return balance    

    def transfer(self, amount, destination_category):
        # Check if we have enough funds
        if self.check_funds(amount):
            # Withdraw from current category
            self.withdraw(amount, f"Transfer to {destination_category.category}")        
            # Deposit to destination category
            destination_category.deposit(amount, f"Transfer from {self.category}")            
            return True
        else:
            return False
        
    def __str__(self):
        output = ""
        title = self.category.center(30, '*')
        output += title + "\n"
        for item in self.ledger:
            description = item["description"][:23]
            amount_str = f"{item['amount']:.2f}"
            output += f"{description}{amount_str.rjust(30-len(description))}\n"
        output += f"Total: {self.get_balance():.2f}"
        return output
        pass


def create_spend_chart(categories):
    # Calculate spending for each category (only withdrawals)
    spent = []
    for category in categories:
        category_spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                category_spent += abs(item["amount"])
        spent.append(category_spent)
    
    # Calculate percentages and round down to nearest 10
    total = sum(spent)
    percentages = [int((s / total) * 100) // 10 * 10 for s in spent]
    
    # Create the chart title
    result = "Percentage spent by category\n"
    
    # Create the percentage bars
    for i in range(100, -1, -10):
        result += str(i).rjust(3) + "| "
        for percentage in percentages:
            if percentage >= i:
                result += "o  "
            else:
                result += "   "
        result += "\n"
    
    # Create the horizontal line
    result += "    " + "-" * (len(categories) * 3 + 1) + "\n"
    
    # Add category names vertically
    # First, find the longest category name
    category_names = [category.category for category in categories]
    max_name_length = max(len(name) for name in category_names)
    
    # Add each letter of the category names
    for i in range(max_name_length):
        result += "     "
        for name in category_names:
            result += name[i] + "  " if i < len(name) else "   "
        if i < max_name_length - 1:
            result += "\n"
            
    return result

create_spend_chart