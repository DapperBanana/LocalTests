
# Initialize inventory dictionary
inventory = {
    'apple': 5,
    'banana': 10,
    'orange': 8,
    'grape': 12
}

# Display menu options
def display_menu():
    print("1. View Inventory")
    print("2. Add to Inventory")
    print("3. Remove from Inventory")
    print("4. Exit")

# View Inventory
def view_inventory():
    print("Current Inventory:")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")

# Add to Inventory
def add_to_inventory():
    item = input("Enter item to add: ")
    quantity = int(input("Enter quantity to add: "))
    
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity

# Remove from Inventory
def remove_from_inventory():
    item = input("Enter item to remove: ")
    quantity = int(input("Enter quantity to remove: "))
    
    if item in inventory:
        if inventory[item] >= quantity:
            inventory[item] -= quantity
        else:
            print("Not enough quantity in inventory.")
    else:
        print("Item not found in inventory.")

# Main program loop
while True:
    display_menu()
    choice = input("Enter choice: ")
    
    if choice == '1':
        view_inventory()
    elif choice == '2':
        add_to_inventory()
    elif choice == '3':
        remove_from_inventory()
    elif choice == '4':
        break
    else:
        print("Invalid choice, please try again.")

print("Exiting program.")
