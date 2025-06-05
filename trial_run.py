
inventory = {}

def add_item(inventory, item_name, quantity):
    if item_name in inventory:
        inventory[item_name] += quantity
    else:
        inventory[item_name] = quantity

def remove_item(inventory, item_name, quantity):
    if item_name in inventory:
        if inventory[item_name] >= quantity:
            inventory[item_name] -= quantity
        else:
            print("Not enough inventory for item:", item_name)
    else:
        print("Item not found in inventory:", item_name)

def check_inventory(inventory):
    print("Current Inventory:")
    for item_name, quantity in inventory.items():
        print(f"{item_name}: {quantity}")

# Main program loop
while True:
    print("\n1. Add item to inventory")
    print("2. Remove item from inventory")
    print("3. Check inventory")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        item_name = input("Enter item name: ")
        quantity = int(input("Enter quantity to add: "))
        add_item(inventory, item_name, quantity)
        print("Item added to inventory.")

    elif choice == '2':
        item_name = input("Enter item name: ")
        quantity = int(input("Enter quantity to remove: "))
        remove_item(inventory, item_name, quantity)
        print("Item removed from inventory.")

    elif choice == '3':
        check_inventory(inventory)

    elif choice == '4':
        break

    else:
        print("Invalid choice. Please try again.")
