# --- Purchase Calculation Script ---

# Request product details from the user
product_name = input("Enter the product to buy: ")
price = int(input("Enter the product price: "))
quantity = float(input("Enter the quantity to buy: "))

# Validation: Ensure both price and quantity are positive numbers
if price < 0:
    print("Invalid numerical value. Please enter a positive number for price.")
elif quantity < 0:
    print("Invalid numerical value. Please enter a positive number for quantity.")
else:
    # Calculate the total cost if inputs are valid
    total_cost = price * quantity
    
    # Display the summary to the user
    print(f"Your total is: {total_cost}")
    print(f"""
    --- Invoice Summary ---
    Product: {product_name} 
    Unit Price: {price}
    Quantity: {quantity}
    Total Cost: {total_cost}
    -----------------------
    """)
