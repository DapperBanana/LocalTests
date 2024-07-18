
inventory = {}

def add_item():
    item = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    inventory[item] = quantity
    print("Item added to inventory.")

def remove_item():
    item = input("Enter item name to remove: ")
    if item in inventory:
        del inventory[item]
        print("Item removed from inventory.")
    else:
        print("Item not found in inventory.")

def display_inventory():
    print("Current Inventory:")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")

while True:
    print("\n1. Add item to inventory")
    print("2. Remove item from inventory")
    print("3. Display inventory")
    print("4. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == '1':
        add_item()
    elif choice == '2':
        remove_item()
    elif choice == '3':
        display_inventory()
    elif choice == '4':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")
