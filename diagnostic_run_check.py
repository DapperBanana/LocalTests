
inventory = {}

def add_item():
    item_name = input("Enter the name of the item: ")
    item_quantity = int(input("Enter the quantity of the item: "))
    inventory[item_name] = item_quantity
    print("Item added to inventory.")

def remove_item():
    item_name = input("Enter the name of the item to remove: ")
    if item_name in inventory:
        del inventory[item_name]
        print("Item removed from inventory.")
    else:
        print("Item not found in inventory.")

def display_inventory():
    print("Inventory:")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")

while True:
    print("\n1. Add item to inventory")
    print("2. Remove item from inventory")
    print("3. Display inventory")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_item()
    elif choice == '2':
        remove_item()
    elif choice == '3':
        display_inventory()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")
