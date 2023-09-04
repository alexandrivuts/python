# Dictionary with information about products
menu = {
    "cake": ["Delicious chocolate cake", 5.0, 500],
    "pastry": ["Flaky pastry with jam", 3.0, 300],
    "muffin": ["Blueberry muffin", 2.0, 200],
    "cookie": ["Classic chocolate chip cookie", 1.0, 1000],
    "cupcake": ["Vanilla cupcake with frosting", 2.5, 400],
    "brownie": ["Fudgy brownie", 3.5, 350],
}

# Main menu
while True:
    print("\nМеню:")
    print("1. Просмотр описания")
    print("2. Просмотр цены")
    print("3. Просмотр количества")
    print("4. Вся информация")
    print("5. Покупка")
    print("6. Выход")

    choice = input("Выберите пункт меню: ")

    if choice == "1":
        product_name = input("Enter the product name: ")
        if product_name in menu:
            print(f"{product_name}: {menu[product_name][0]}")
        else:
            print("Product not found in the menu.")

    elif choice == "2":
        # View price
        product_name = input("Enter the product name: ")
        if product_name in menu:
            print(f"{product_name} price: ${menu[product_name][1]} per 100g")
        else:
            print("Product not found in the menu.")

    elif choice == "3":
        # View quantity
        product_name = input("Enter the product name: ")
        if product_name in menu:
            print(f"{product_name} quantity: {menu[product_name][2]}g")
        else:
            print("Product not found in the menu.")

    elif choice == "4":
        # All information
        for product, info in menu.items():
            print(f"{product}: {info[0]}, Price: ${info[1]} per 100g, Quantity: {info[2]}g")

    elif choice == "5":
        # Purchase
        total_price = 0
        while True:
            product_name = input("Enter the product name (n to exit): ")
            if product_name == "n":
                break
            if product_name in menu:
                try:
                    quantity = int(input(f"Enter the quantity of {product_name} (in grams): "))
                    if quantity <= menu[product_name][2]:
                        price_per_100g = menu[product_name][1]
                        total_price += (price_per_100g / 100) * quantity
                        menu[product_name][2] -= quantity
                    else:
                        print("Not enough product in stock.")
                except ValueError:
                    print("Please enter a valid quantity.")
            else:
                print("Product not found in the menu.")
        print(f"Total purchase price: ${total_price:.2f}")

    elif choice == "6":
        # Exit
        print("Thank you for visiting! Goodbye.")
        break

    else:
        print("Invalid choice. Please select a menu item from 1 to 6.")
