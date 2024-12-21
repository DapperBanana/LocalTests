
# Create an empty inventory dictionary
inventory = {}

def add_item(name, quantity):
    if name in inventory:
        inventory[name] += quantity
    else:
        inventory[name] = quantity

def remove_item(name, quantity):
    if name in inventory:
        if inventory[name] >= quantity:
            inventory[name] -= quantity
        else:
            print("Not enough quantity in inventory")
    else:
        print("Item not found in inventory")

def display_inventory():
    print("Current Inventory:")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")

# Main program loop
while True:
    print("\n1. Add item to inventory")
    print("2. Remove item from inventory")
    print("3. Display inventory")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        add_item(name, quantity)
    elif choice == '2':
        name = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        remove_item(name, quantity)
    elif choice == '3':
        display_inventory()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")

print("Exiting program.")
