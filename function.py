# Step 1: Define the function.
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent/100)
        final_price = price - discount_amount
        return final_price
    else:
        return price
    

# Step 2: Prompt the user for input
# Convert inputs to float since prices and percentages can be decimals
original_price = float(input("Enter the original price of the item: "))
discount = float(input("Enter the discount percentage: "))

# Step 3: Call the function
final_price = calculate_discount(original_price, discount)

# Step 4: The results
if discount >= 20:
    print(f"Discount applied! Final price: ${final_price:.2f}")

else:
    print(f"No discount applied! Final price: ${final_price:.2f}")