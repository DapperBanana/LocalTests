
# define a function to add items to the inventory
def add_item(inventory, item_name, quantity):
    if item_name in inventory:
        inventory[item_name] += quantity
    else:
        inventory[item_name] = quantity

# define a function to remove items from the inventory
def remove_item(inventory, item_name, quantity):
    if item_name in inventory and inventory[item_name] >= quantity:
        inventory[item_name] -= quantity
    else:
        print("Error: Not enough quantity of {} in inventory.".format(item_name))

# define a function to display the inventory
def display_inventory(inventory):
    print("Current Inventory:")
    for item, quantity in inventory.items():
        print("{}: {}".format(item, quantity))

# initialize an empty inventory
inventory = {}

# menu loop
while True:
    print("\n1. Add item to inventory")
    print("2. Remove item from inventory")
    print("3. Display inventory")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item_name = input("Enter item name: ")
        quantity = int(input("Enter quantity to add: "))
        add_item(inventory, item_name, quantity)
    elif choice == "2":
        item_name = input("Enter item name: ")
        quantity = int(input("Enter quantity to remove: "))
        remove_item(inventory, item_name, quantity)
    elif choice == "3":
        display_inventory(inventory)
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")
