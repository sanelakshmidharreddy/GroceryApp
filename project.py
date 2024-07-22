# Initialize an empty inventory dictionary
inventory = {}

# Function to add a new product to the inventory
def add_product():
    name = input("Enter product name: ")
    category = input("Enter product category: ")
    quantity = int(input("Enter product quantity: "))

    # Check if the product already exists
    if name in inventory:
        print(f"{name} already exists in the inventory.")
    else:
        # Add the product to the inventory dictionary
        inventory[name] = {'category': category, 'quantity': quantity}
        print(f"{name} added to inventory.")


# Function to remove a product from the inventory
def remove_product():
    name = input("Enter product name to remove: ")

    # Check if the product exists
    if name in inventory:
        del inventory[name]
        print(f"{name} removed from inventory.")
    else:
        print(f"{name} is not found in the inventory.")


# Function to update details of a product in the inventory
def update_product():
    name = input("Enter product name to update: ")

    # Check if the product exists
    if name in inventory:
        category = input(f"Enter new category for {name}: ")
        quantity = int(input(f"Enter new quantity for {name}: "))
        # Update category and quantity of the product
        inventory[name]['category'] = category
        inventory[name]['quantity'] = quantity
        print(f"{name} updated successfully.")
    else:
        print(f"{name} is not found in the inventory.")


# Function to track the quantity of a product in the inventory
def track_quantity():
    name = input("Enter product name to track quantity: ")

    # Check if the product exists
    if name in inventory:
        print(f"Current quantity of {name} is: {inventory[name]['quantity']}")
    else:
        print(f"{name} is not found in the inventory.")


# Function to categorize a product in the inventory
def categorize_product():
    name = input("Enter product name to categorize: ")

    # Check if the product exists
    if name in inventory:
        print(f"{name} belongs to category: {inventory[name]['category']}")
    else:
        print(f"{name} is not found in the inventory.")


# Function to generate an inventory report
def generate_inventory_report():
    print("Current Inventory:")
    for name, details in inventory.items():
        print(f"Product: {name}, Category: {details['category']}, Quantity: {details['quantity']}")


# Function to search for a product in the inventory
def search_product():
    name = input("Enter product name to search: ")

    # Check if the product exists
    if name in inventory:
        print(f"Product: {name}, Category: {inventory[name]['category']}, Quantity: {inventory[name]['quantity']}")
    else:
        print(f"{name} is not found in the inventory.")


# Main loop for the inventory management system
while True:
    # Display menu options
    print("*" * 50)
    print("         Welcome To G4 Super Mart")
    print("*"*50)
    print("\n===== Inventory Management System =====")
    print("1. Add Product")
    print("2. Remove Product")
    print("3. Update Product")
    print("4. Track Product Quantity")
    print("5. Categorize Product")
    print("6. Generate Inventory Report")
    print("7. Search Product")
    print("8. Exit")

    # Get user's choice
    choice = input("Enter your choice (1-8): ")
    # Perform actions based on user's choice
    if choice == '1':
        add_product()
    elif choice == '2':
        remove_product()
    elif choice == '3':
        update_product()
    elif choice == '4':
        track_quantity()
    elif choice == '5':
        categorize_product()
    elif choice == '6':
        generate_inventory_report()
    elif choice == '7':
        search_product()
    elif choice == '8':
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 8")

