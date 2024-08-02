def get_product_info():
    products = []
    while True:
        # Collect user input
        product_id = input("\n\nEnter the product ID (or type 'done' to finish): ")
        if product_id.lower() == 'done':
            break
        
        name_product = input("Enter the product name: ")
        try:
            price = float(input("Enter the product price:"))
        except ValueError:
            print("Invalid price. Please enter a numerical value.")
            continue

        # Create a tuple and add it to the list
        product_info = (product_id, name_product, price)
        products.append(product_info)
    
    return products

products_purchased = get_product_info() # Get product information from the user

print("This is the list of products:") # Print the product details
for product_id, name_product, price in products_purchased:
    print(f"""ID: {product_id}, Name of the product purchased is {name_product},
              Price of the product: ${price:.2f}.
    """)
