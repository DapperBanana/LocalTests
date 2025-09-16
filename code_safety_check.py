
# Initialize an empty inventory dictionary
inventory = {}

def add_item(item_name, quantity):
    if item_name in inventory:
        inventory[item_name] += quantity
    else:
        inventory[item_name] = quantity

def remove_item(item_name, quantity):
    if item_name in inventory:
        if inventory[item_name] >= quantity:
            inventory[item_name] -= quantity
        else:
            print("Not enough quantity of", item_name, "in inventory")
    else:
        print("Item", item_name, "not found in inventory")

def view_inventory():
    if len(inventory) == 0:
        print("Inventory is empty")
    else:
        print("Current Inventory:")
        for item, quantity in inventory.items():
            print(item, ":", quantity)

# Main program loop
while True:
    print("\nInventory Management System")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Inventory")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        item_name = input("Enter item name: ")
        quantity = int(input("Enter quantity to add: "))
        add_item(item_name, quantity)
        print("Item added to inventory")

    elif choice == '2':
        item_name = input("Enter item name: ")
        quantity = int(input("Enter quantity to remove: "))
        remove_item(item_name, quantity)

    elif choice == '3':
        view_inventory()

    elif choice == '4':
        print("Exiting program")
        break

    else:
        print("Invalid choice. Please try again.")
