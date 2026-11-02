import math

print("CAMPUS EVENT FINANCIAL PLANNING")

# Input details
participants = int(input("Enter expected participants: "))

venue = float(input("Enter venue cost: "))
equipment = float(input("Enter equipment cost: "))
transport = float(input("Enter transport cost: "))

catering = float(input("Enter catering cost per participant: "))
certificate = float(input("Enter certificate cost per participant: "))

sponsorship = float(input("Enter sponsorship amount: "))
registration_fee = float(input("Enter registration fee per participant: "))

# Fixed and variable costs
fixed_cost = venue + equipment + transport

variable_cost = catering + certificate

total_variable_cost = variable_cost * participants

# Total expenses
total_cost = fixed_cost + total_variable_cost

# Required participant contribution
amount_to_collect = max(total_cost - sponsorship, 0)

if participants > 0:
    contribution = amount_to_collect / participants
else:
    contribution = 0

# Registration income
registration_income = registration_fee * participants

# Sponsorship shortfall
shortfall = max(total_cost - sponsorship - registration_income, 0)

# Profit or loss
balance = sponsorship + registration_income - total_cost

# Break-even calculation
if registration_fee > variable_cost:
    required_registrations = math.ceil(
        max(fixed_cost - sponsorship, 0)
        / (registration_fee - variable_cost)
    )
else:
    required_registrations = None

# Display report
print("\n------ EVENT FINANCIAL REPORT ------")

print("Fixed Cost:", fixed_cost)
print("Variable Cost per Participant:", variable_cost)
print("Total Variable Cost:", total_variable_cost)
print("Total Event Cost:", total_cost)

print("Required Contribution per Participant:",
      round(contribution, 2))

print("Registration Income:", registration_income)
print("Sponsorship Amount:", sponsorship)
print("Sponsorship Shortfall:", shortfall)

if required_registrations is not None:
    print("Minimum Registrations for Break-even:",
          required_registrations)
else:
    print("Break-even is not possible at this registration fee.")

if balance > 0:
    print("Event Profit:", balance)
elif balance < 0:
    print("Event Loss:", abs(balance))
else:
    print("Event is at Break-even.")

print("------------------------------------")
