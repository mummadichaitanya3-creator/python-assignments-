print("ELECTRICITY BILL CALCULATOR")

name = input("Enter Consumer Name: ")

bills = []

for month in range(1, 4):

    print("\nMonth", month)

    units = int(input("Enter electricity units: "))

    # Calculate electricity charges
    if units <= 100:
        amount = units * 2

    elif units <= 200:
        amount = (100 * 2) + (units - 100) * 3

    elif units <= 300:
        amount = (100 * 2) + (100 * 3) + (units - 200) * 5

    else:
        amount = (100 * 2) + (100 * 3) + (100 * 5) + (units - 300) * 7

    # Fixed charges
    amount = amount + 50

    # Surcharge
    amount = amount + (amount * 0.05)

    # Rebate
    if units < 100:
        amount = amount - (amount * 0.10)

    bills.append(amount)

    print("Electricity Bill: Rs.", round(amount, 2))


# Compare monthly bills
print("\nMONTHLY BILL COMPARISON")

for i in range(3):
    print("Month", i + 1, ":", round(bills[i], 2))

# Identify unusual increase
for i in range(1, 3):

    increase = bills[i] - bills[i - 1]

    if increase > bills[i - 1] * 0.20:
        print("Unusual increase detected in Month", i + 1)

print("\nThank You!")
