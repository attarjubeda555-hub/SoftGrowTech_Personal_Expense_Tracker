import csv
from datetime import datetime
import matplotlib.pyplot as plt

FILE_NAME = "expenses.csv"

# Initialize file
def initialize_file():
    try:
        with open(FILE_NAME, 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Type", "Category", "Amount"])
    except FileExistsError:
        pass

# Add entry
def add_entry(entry_type):
    date = datetime.now().strftime("%Y-%m-%d")
    category = input("Enter category (Food, Travel, Salary, etc.): ")
    amount = float(input("Enter amount: "))

    with open(FILE_NAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, entry_type, category, amount])

    print("Entry added successfully!\n")

# View entries
def view_entries():
    try:
        with open(FILE_NAME, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No records found.\n")

# Show summary
def show_summary():
    income = 0
    expense = 0

    try:
        with open(FILE_NAME, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["Type"] == "Income":
                    income += float(row["Amount"])
                else:
                    expense += float(row["Amount"])

        print("\nSummary:")
        print(f"Total Income: ₹{income}")
        print(f"Total Expense: ₹{expense}")
        print(f"Balance: ₹{income - expense}\n")

    except FileNotFoundError:
        print("No data available.\n")

# Pie Chart Function
def show_pie_chart():
    categories = {}

    try:
        with open(FILE_NAME, 'r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row["Type"] == "Expense":
                    category = row["Category"]
                    amount = float(row["Amount"])

                    if category in categories:
                        categories[category] += amount
                    else:
                        categories[category] = amount

        if not categories:
            print("No expense data to show.\n")
            return

        labels = list(categories.keys())
        values = list(categories.values())

        plt.figure()
        plt.pie(values, labels=labels, autopct='%1.1f%%')
        plt.title("Expense Distribution by Category")
        plt.show()

    except FileNotFoundError:
        print("No data available.\n")

# Menu
def menu():
    initialize_file()

    while True:
        print("====== Personal Expense Tracker ======")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View All Records")
        print("4. Show Summary")
        print("5. Show Pie Chart")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_entry("Income")
        elif choice == '2':
            add_entry("Expense")
        elif choice == '3':
            view_entries()
        elif choice == '4':
            show_summary()
        elif choice == '5':
            show_pie_chart()
        elif choice == '6':
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice. Try again.\n")

# Run program
menu()