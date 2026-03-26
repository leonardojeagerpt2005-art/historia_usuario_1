# --- Purchase Calculation Script ---
continuar_ciclo = True
# Request product details from the user
while continuar_ciclo :
    product_name = input("Enter the product to buy: ")
    price = float(input("Enter the product price: "))
    quantity = int(input("Enter the quantity to buy: "))

    # Validation: Ensure both price and quantity are positive numbers
    if price <= 0:
        print("Invalid numerical value. Please enter a positive number for price.")
        continue
    elif quantity <= 0:
        print("Invalid numerical value. Please enter a positive number for quantity.")
        continue
    else:
        # Calculate the total cost if inputs are valid
        total_cost = price * quantity
        continuar_ciclo = input("Do you want to calculate another product? (yes/no): ").strip().lower()
        if continuar_ciclo == 'no':
            continuar_ciclo = False
        
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
