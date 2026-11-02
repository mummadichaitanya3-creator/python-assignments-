
print("MANUFACTURING COST ANALYSIS")

# Product details
name = input("Enter Product Name: ")

quantity = int(input("Enter Production Quantity: "))

material = float(input("Enter Material Cost per Unit: "))

labour = float(input("Enter Labour Cost per Unit: "))

machine = float(input("Enter Machine Cost per Unit: "))

selling = float(input("Enter Selling Price per Unit: "))

# Validate inputs
if quantity <= 0 or material < 0 or labour < 0 or machine < 0 or selling < 0:

    print("Invalid Input!")

else:

    # Calculate costs
    material_cost = quantity * material

    labour_cost = quantity * labour

    wastage = material_cost * 0.05

    machine_cost = quantity * machine

    # Total manufacturing cost
    total_cost = material_cost + labour_cost + wastage + machine_cost

    # Total selling price
    total_selling = quantity * selling

    # Profit calculation
    profit = total_selling - total_cost

    # Profit percentage
    if total_cost > 0:
        profit_percentage = (profit / total_cost) * 100
    else:
        profit_percentage = 0

    # Check profit target
    print("\n----- MANUFACTURING REPORT -----")

    print("Product Name:", name)
    print("Production Quantity:", quantity)

    print("Material Cost: Rs.", material_cost)
    print("Labour Cost: Rs.", labour_cost)
    print("Wastage Cost: Rs.", wastage)
    print("Machine Cost: Rs.", machine_cost)

    print("--------------------------------")

    print("Total Manufacturing Cost: Rs.", total_cost)

    print("Total Selling Price: Rs.", total_selling)

    print("Profit / Loss: Rs.", profit)

    print("Profit Percentage:", round(profit_percentage, 2), "%")

    if profit_percentage >= 20:
        print("Result: Profit Target Achieved")

    else:
        print("Result: Profit Target Not Achieved")

    print("--------------------------------")
    print("Thank You!")
