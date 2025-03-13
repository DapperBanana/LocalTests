
# Initialize an empty inventory dictionary
inventory = {}

def display_menu():
    print("1. Add item to inventory")
    print("2. Remove item from inventory")
    print("3. View inventory")
    print("4. Exit")

def add_item():
    item_name = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    
    if item_name in inventory:
        inventory[item_name] += quantity
    else:
        inventory[item_name] = quantity

def remove_item():
    item_name = input("Enter item name to remove: ")
    
    if item_name in inventory:
        del inventory[item_name]
    else:
        print("Item not found in inventory")

def view_inventory():
    print("Current inventory:")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")

# Main program loop
while True:
    display_menu()
    choice = input("Enter choice: ")
    
    if choice == "1":
        add_item()
    elif choice == "2":
        remove_item()
    elif choice == "3":
        view_inventory()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")
