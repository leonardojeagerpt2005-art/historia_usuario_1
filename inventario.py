continue_cyclo = True

while continue_cyclo:
    print("=" * 50)
    product_name = input("Enter the product to buy: ")
    print("=" * 50)

    # 🔹 Price validation loop
    valid_price = True
    while valid_price:
        price = float(input("Enter the product price: "))
        if price <= 0:
            print("=" * 50)
            print("Invalid numerical value. Please enter a positive number for price.")
            print("=" * 50)
        else:
            valid_price = False

    print("=" * 50)

    # 🔹 Quantity validation loop
    valid_quantity = True
    while  valid_quantity:
        quantity = int(input("Enter the quantity to buy: "))
        if quantity <= 0:
            print("=" * 50)
            print("Invalid numerical value. Please enter a positive number for quantity.")
            print("=" * 50)
        else:
            valid_quantity = False

    print("=" * 50)

    total_cost = price * quantity

    print(f"Your total is: {total_cost}")
    print("=" * 50)
    print(f"""
    --- Invoice Summary ---
    Product: {product_name} 
    Unit Price: {price}
    Quantity: {quantity}
    Total Cost: {total_cost}
    -----------------------
    """)
    print("=" * 50)

    answer = input("Do you want to calculate another product? (yes/no): ").strip().lower()
    if answer == 'no':
        continue_cyclo = False