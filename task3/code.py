
print("HOSPITAL BILLING SYSTEM")

name = input("Enter Patient Name: ")
age = int(input("Enter Patient Age: "))

consultation = float(input("Enter Consultation Charges: "))
diagnostic = float(input("Enter Diagnostic Charges: "))
treatment = float(input("Enter Treatment Charges: "))

# Validate charges
if age < 0 or consultation < 0 or diagnostic < 0 or treatment < 0:
    print("Invalid Input!")

else:

    # Calculate total bill
    total = consultation + diagnostic + treatment

    # Apply concession
    if age < 12:
        discount = total * 0.10

    elif age >= 60:
        discount = total * 0.15

    else:
        discount = 0

    # Calculate final bill
    final_bill = total - discount

    # Patient classification
    if final_bill < 1000:
        category = "Low Payment"

    elif final_bill <= 3000:
        category = "Medium Payment"

    else:
        category = "High Payment"

    # Display bill
    print("\n----- HOSPITAL BILL -----")

    print("Patient Name:", name)
    print("Patient Age:", age)
    print("Total Bill: Rs.", total)
    print("Discount: Rs.", discount)
    print("Final Bill: Rs.", final_bill)
    print("Patient Classification:", category)

    print("Thank You!")
