
# Initialize inventory dictionary
inventory = {}

# Display menu options
def display_menu():
    print("1. Add item to inventory")
    print("2. Remove item from inventory")
    print("3. View inventory")
    print("4. Exit")

# Add item to inventory
def add_item():
    item_name = input("Enter item name: ")
    item_quantity = int(input("Enter item quantity: "))
    inventory[item_name] = item_quantity

# Remove item from inventory
def remove_item():
    item_name = input("Enter item name to remove: ")
    if item_name in inventory:
        del inventory[item_name]
        print("Item removed from inventory")
    else:
        print("Item not found in inventory")

# View inventory
def view_inventory():
    print("Current inventory:")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")

# Main program loop
while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        add_item()
    elif choice == '2':
        remove_item()
    elif choice == '3':
        view_inventory()
    elif choice == '4':
        print("Exiting program")
        break
    else:
        print("Invalid choice, please try again")
