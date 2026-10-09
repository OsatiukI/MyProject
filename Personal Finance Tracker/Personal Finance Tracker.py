def add_transaction():
    transaction_type = input("Type of transaction: ")
    if transaction_type not in ("income", "expense"):
        print("Invalid transaction type")
        return
    while True:
        try:
            amount = float(input("Amount: "))
            if amount <= 0:
                print("Invalid amount")
            else:
                break
        except ValueError:
            print("Invalid amount")
    while True:
        category = input("Category: ")
        if category.strip() == "":
            print("Invalid category")
        else:
            break
    description = input("Description: ")
    new_dict = {"transaction_type": transaction_type, "amount": amount, "category": category, "description": description}
    transactions.append(new_dict)


def calculate_balance():
    balance = 0
    for transaction in transactions:
        if transaction["transaction_type"] == "income":
            balance += transaction["amount"]
        elif transaction["transaction_type"] == "expense":
            balance -= transaction["amount"]
        else:
            print("Invalid transaction type")
    return balance


def calculate_expenses():
    total_expenses = 0
    for transaction in transactions:
        if transaction["transaction_type"] == "expense":
            total_expenses += transaction["amount"]
    return total_expenses


def calculate_expenses_by_category(category):
    total_expenses = 0
    for transaction in transactions:
        if transaction["transaction_type"] == "expense" and transaction["category"] == category:
            total_expenses += transaction["amount"]
    return total_expenses


transactions = []

while True:
    print("1. Add transaction")
    print("2. Show transactions")
    print("3. Show balance")
    print("4. Show total expenses")
    print("5. Show expenses by category")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_transaction()
    elif choice == "2":
        if not transactions:
            print("No transactions")
        else:
            for transaction in transactions:
                print(f"Type: {transaction['transaction_type'].capitalize()}")
                print(f"Amount: {transaction['amount']:.2f}")
                print(f"Category: {transaction['category']}")
                print(f"Description: {transaction['description']}")
                print("-" * 25)
    elif choice == "3":
        balance = calculate_balance()
        print(f"Current balance: {balance:.2f}")
    elif choice == "4":
        expenses = calculate_expenses()
        print(f"Total expenses: {expenses:.2f}")
    elif choice == "5":
        answer = input("Select a category: ")
        expenses = calculate_expenses_by_category(answer)
        print(f"Expenses for {answer}: {expenses:.2f}")
    elif choice == "6":
        break
    else:
        print("Invalid choice")


