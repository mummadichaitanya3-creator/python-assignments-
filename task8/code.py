print("RAILWAY FARE CALCULATOR")

n = int(input("Enter Number of Passengers: "))

total_fare = 0

for i in range(n):

    print("\nPassenger", i + 1)

    name = input("Enter Passenger Name: ")
    age = int(input("Enter Age: "))
    distance = int(input("Enter Distance in KM: "))

    print("1. Sleeper")
    print("2. AC 3 Tier")
    print("3. AC 2 Tier")

    choice = int(input("Select Travel Class: "))

    # Validate input
    if age < 0 or distance <= 0 or choice not in [1, 2, 3]:
        print("Invalid Input!")
        continue

    # Distance fare
    if distance <= 100:
        fare = distance * 2

    elif distance <= 300:
        fare = distance * 3

    elif distance <= 500:
        fare = distance * 4

    else:
        fare = distance * 5

    # Class charges
    if choice == 1:
        class_charge = 50
        reservation = 20
        class_name = "Sleeper"

    elif choice == 2:
        class_charge = 150
        reservation = 40
        class_name = "AC 3 Tier"

    else:
        class_charge = 250
        reservation = 60
        class_name = "AC 2 Tier"

    fare = fare + class_charge

    # Age concession
    if age < 5:
        discount = fare

    elif age <= 12:
        discount = fare * 0.50

    elif age >= 60:
        discount = fare * 0.30

    else:
        discount = 0

    fare = fare - discount

    # Add reservation fee
    fare = fare + reservation

    # Cancellation
    cancel = input("Cancel Ticket? (yes/no): ")

    if cancel.lower() == "yes":

        time = int(input("Hours before departure: "))

        if time < 0:
            print("Invalid cancellation time!")
            continue

        elif time <= 24:
            penalty = fare * 0.25

        else:
            penalty = fare * 0.10

        fare = penalty
        print("Cancellation Penalty: Rs.", round(penalty, 2))

    else:
        print("Ticket Confirmed")

    total_fare = total_fare + fare

    # Display passenger details
    print("\n----- PASSENGER BILL -----")

    print("Passenger Name:", name)
    print("Age:", age)
    print("Distance:", distance, "KM")
    print("Travel Class:", class_name)
    print("Final Fare: Rs.", round(fare, 2))


print("\n===== RAILWAY BILL =====")
print("Total Passengers:", n)
print("Total Railway Amount: Rs.", round(total_fare, 2))
print("Thank You!")
