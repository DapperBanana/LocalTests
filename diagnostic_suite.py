
# Basic text-based inventory management system

inventory = {}

def add_item():
    name = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    
    if name in inventory:
        inventory[name] += quantity
    else:
        inventory[name] = quantity
        
    print(f"{quantity} {name} added to inventory.")

def remove_item():
    name = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    
    if name in inventory:
        if inventory[name] >= quantity:
            inventory[name] -= quantity
            print(f"{quantity} {name} removed from inventory.")
        else:
            print("Not enough quantity in inventory.")
    else:
        print("Item not found in inventory.")

def view_inventory():
    print("Current Inventory:")
    for item in inventory:
        print(f"{item}: {inventory[item]}")

while True:
    print("\nInventory Management System")
    print("1. Add item to inventory")
    print("2. Remove item from inventory")
    print("3. View inventory")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        add_item()
    elif choice == '2':
        remove_item()
    elif choice == '3':
        view_inventory()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")
