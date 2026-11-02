print("RETAIL BILLING SYSTEM")

name = input("Enter Customer Name: ")

n = int(input("Enter Number of Products: "))

total = 0

for i in range(n):

    print("\nProduct", i + 1)

    product = input("Enter Product Name: ")
    category = input("Enter Category (food/electronics/clothing): ")
    price = float(input("Enter Product Price: "))
    quantity = int(input("Enter Quantity: "))

    # Validate input
    if price < 0 or quantity <= 0:
        print("Invalid Product Details!")
        continue

    # Calculate product amount
    amount = price * quantity

    # Category tax
    if category.lower() == "food":
        tax = amount * 0.05

    elif category.lower() == "electronics":
        tax = amount * 0.18

    elif category.lower() == "clothing":
        tax = amount * 0.12

    else:
        print("Invalid Category!")
        continue

    product_total = amount + tax

    total = total + product_total

    print("Product:", product)
    print("Amount:", amount)
    print("Tax:", tax)
    print("Product Total:", product_total)


# Discount calculation
if total < 1000:
    discount = 0

elif total <= 3000:
    discount = total * 0.05

else:
    discount = total * 0.10

# Maximum discount limit
if discount > 500:
    discount = 500

# Final bill
final_bill = total - discount

# Display invoice
print("\n===== RETAIL INVOICE =====")

print("Customer Name:", name)
print("Total Amount: Rs.", round(total, 2))
print("Discount: Rs.", round(discount, 2))
print("Final Bill: Rs.", round(final_bill, 2))

print("==========================")
print("Thank You! Visit Again!")
