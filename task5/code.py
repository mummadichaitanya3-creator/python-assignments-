print("MULTI-CURRENCY TRAVEL BUDGET ANALYSIS")

# Traveller details
name = input("Enter Traveller Name: ")

budget = float(input("Enter Travel Budget in INR: "))

n = int(input("Enter Number of Expense Categories: "))

total = 0
expenses = {}

# Exchange rates
rates = {
    "INR": 1,
    "USD": 85,
    "EUR": 92,
    "GBP": 110
}

# Enter expenses
for i in range(n):

    print("\nExpense", i + 1)

    category = input("Enter Category: ")

    currency = input("Enter Currency (INR/USD/EUR/GBP): ").upper()

    amount = float(input("Enter Expense Amount: "))

    # Validate input
    if amount < 0 or currency not in rates:
        print("Invalid Input!")
        continue

    # Currency conversion
    converted = amount * rates[currency]

    # Conversion fee
    fee = converted * 0.02

    # Total expense
    final_amount = converted + fee

    expenses[category] = expenses.get(category, 0) + final_amount

    total = total + final_amount

    print("Converted Amount: Rs.", round(converted, 2))
    print("Conversion Fee: Rs.", round(fee, 2))
    print("Total Expense: Rs.", round(final_amount, 2))


# Budget comparison
print("\n===== TRAVEL BUDGET REPORT =====")

print("Traveller Name:", name)
print("Travel Budget: Rs.", budget)
print("Total Expenses: Rs.", round(total, 2))

if total < budget:
    print("Status: Within Budget")

elif total == budget:
    print("Status: Budget Fully Used")

else:
    print("Status: Budget Exceeded")

# Largest expense category
if expenses:

    largest = max(expenses, key=expenses.get)

    print("Largest Expense Category:", largest)

    print("Largest Expense Amount: Rs.", round(expenses[largest], 2))

else:
    print("No Valid Expenses Entered")

print("Remaining Budget: Rs.", round(budget - total, 2))

print("\nThank You!")
