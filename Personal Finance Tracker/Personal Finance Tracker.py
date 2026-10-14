import json
import math


def validate_transaction(transaction):
    if not isinstance(transaction, dict):
        return False
    if not all(key in transaction for key in ["transaction_type", "amount", "category", "description"]):
        return False
    if transaction["transaction_type"] not in ("income", "expense"):
        return False
    if isinstance(transaction["amount"], bool):
        return False
    if not isinstance(transaction["amount"], (int, float)):
        return False
    if not math.isfinite(transaction["amount"]):
        return False
    if transaction["amount"] <= 0:
        return False
    if not isinstance(transaction["category"], str) or not transaction["category"].strip():
        return False
    if not isinstance(transaction["description"], str) or not transaction["description"].strip():
        return False
    return True




def calculate_income():
    total = 0
    for transaction in transactions:
        if transaction["transaction_type"] == "income":
            total += transaction["amount"]
    return total


def display_transactions():
    for number, transaction in enumerate(transactions, 1):
        print(f"{number}")
        print(f"Type: {transaction['transaction_type'].capitalize()}")
        print(f"Amount: {transaction['amount']:.2f}")
        print(f"Category: {transaction['category']}")
        print(f"Description: {transaction['description']}")
        print("-" * 25)


def edit_transaction():
    if not data_loaded:
        print("Cannot modify transactions: data file could not be loaded")
        return
    elif transactions == []:
        print("No transactions")
    else:
        display_transactions()
        answer = input("Enter your choice: ")
        try:
            choice = int(answer)
        except ValueError:
            print("Invalid input")
            return
        if choice <= 0 or choice > len(transactions):
            print("Invalid choice")
            return
        else:
            selected_transaction = transactions[choice - 1]
            print("1. Type")
            print("2. Amount")
            print("3. Category")
            print("4. Description")
            field_answer = input("Which field do you want to edit? ")
            try:
                field_choice = int(field_answer)
            except ValueError:
                print("Invalid input")
                return
            if field_choice <=0 or field_choice > 4:
                print("Invalid choice")
                return
            if field_choice == 1:
                answer_type = input("Type of field: ")
                if answer_type not in ("income", "expense"):
                    print("Invalid type")
                    return
                selected_transaction["transaction_type"] = answer_type
            if field_choice == 2:
                try:
                    answer_amount = float(input("Amount: "))
                except ValueError:
                    print("Invalid input")
                    return
                if not math.isfinite(answer_amount) or answer_amount <= 0:
                    print("Invalid amount")
                    return
                selected_transaction["amount"] = answer_amount
            if field_choice == 3:
                 answer_category = input("Category: ")
                 answer_category = answer_category.strip()
                 if not answer_category:
                     print("Category cannot be empty")
                     return
                 selected_transaction["category"] = answer_category
            if field_choice == 4:
                answer_description = input("Description: ")
                answer_description = answer_description.strip()
                if not answer_description:
                    print("Description cannot be empty")
                    return
                selected_transaction["description"] = answer_description
            save_transactions()
            print("Transaction updated successfully!")


def delete_transaction():
    if not data_loaded:
        print("Cannot modify transactions: data file could not be loaded")
        return
    elif transactions == []:
        print("No transactions")
    else:
        display_transactions()
        print("Which transaction do you want to delete?: ", )
        answer = input("Enter your choice: ")
        try:
            choice = int(answer)
        except ValueError:
            print("Invalid input")
            return
        if choice <= 0 or choice > len(transactions):
            print("Invalid choice")
        else:
            del_transaction = transactions.pop(choice - 1)
            print("Transaction deleted successfully!")
            print(f"Type: {del_transaction['transaction_type'].capitalize()}")
            print(f"Amount: {del_transaction['amount']:.2f}")
            print(f"Category: {del_transaction['category']}")
            print(f"Description: {del_transaction['description']}")
            save_transactions()


def load_transactions():
    try:
        with open("transactions.json", "r") as file:
            transactions = json.load(file)
        if not isinstance(transactions, list):
            print("Error: transactions.json must contain a list.")
            return [], False
        if not all(validate_transaction(transaction) for transaction in transactions):
            print("Error: transactions.json contains invalid transactions.")
            return [], False
        data_loaded = True
    except FileNotFoundError:
        transactions = []
        data_loaded = True
    except json.decoder.JSONDecodeError:
        print("Error: transactions.json is corrupted. Restore the file before continuing.")
        transactions = []
        data_loaded = False
    return transactions, data_loaded


def save_transactions():
    with open("transactions.json", "w") as file:
        json.dump(transactions, file)


def add_transaction():
    if not data_loaded:
        print("Cannot add transaction: data file could not be loaded")
        return
    transaction_type = input("Type of transaction: ")
    if transaction_type not in ("income", "expense"):
        print("Invalid transaction type")
        return
    while True:
        try:
            amount = float(input("Amount: "))
            if not math.isfinite(amount) or amount <= 0:
                print("Invalid amount")
            else:
                break
        except ValueError:
            print("Invalid amount")
    while True:
        category = input("Category: ").strip()
        if not category:
            print("Invalid category")
        else:
            break
    while True:
        description = input("Description: ").strip()
        if not description:
            print("Invalid description")
        else:
            break
    new_dict = {"transaction_type": transaction_type, "amount": amount, "category": category, "description": description}
    transactions.append(new_dict)
    save_transactions()


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


transactions, data_loaded = load_transactions()
if __name__ == "__main__":
    while True:
        print("1. Add transaction")
        print("2. Show transactions")
        print("3. Show balance")
        print("4. Show total expenses")
        print("5. Show expenses by category")
        print("6. Delete transaction")
        print("7. Edit transaction")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_transaction()
        elif choice == "2":
            if not transactions:
                print("No transactions")
            else:
                display_transactions()
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
            delete_transaction()
        elif choice == "7":
            edit_transaction()
        elif choice == "8":
            break
        else:
            print("Invalid choice")

