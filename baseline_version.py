
inventory = {}

def display_menu():
    print("\n1. Add item to inventory")
    print("2. Remove item from inventory")
    print("3. View inventory")
    print("4. Quit")

def add_item():
    item_name = input("Enter item name: ")
    item_quantity = int(input("Enter item quantity: "))
    inventory[item_name] = item_quantity
    print(f"{item_name} added to inventory.")
    
def remove_item():
    item_name = input("Enter item name to remove: ")
    if item_name in inventory:
        del inventory[item_name]
        print(f"{item_name} removed from inventory.")
    else:
        print("Item not found in inventory.")
    
def view_inventory():
    print("\nInventory:")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")
    
while True:
    display_menu()
    choice = input("Enter choice: ")
    
    if choice == '1':
        add_item()
    elif choice == '2':
        remove_item()
    elif choice == '3':
        view_inventory()
    elif choice == '4':
        print("Exiting inventory management system.")
        break
    else:
        print("Invalid choice. Please try again.")
