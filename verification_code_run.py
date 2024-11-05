
# Initialize an empty inventory dictionary
inventory = {}

def add_item():
    item_name = input("Enter item name: ")
    item_quantity = int(input("Enter item quantity: "))
    
    if item_name in inventory:
        inventory[item_name] += item_quantity
    else:
        inventory[item_name] = item_quantity
    
    print(f"{item_quantity} {item_name}(s) added to inventory")

def remove_item():
    item_name = input("Enter item name: ")
    item_quantity = int(input("Enter quantity to remove: "))
    
    if item_name in inventory:
        if inventory[item_name] >= item_quantity:
            inventory[item_name] -= item_quantity
            print(f"{item_quantity} {item_name}(s) removed from inventory")
        else:
            print("Not enough quantity in inventory")
    else:
        print("Item not found in inventory")

def view_inventory():
    print("Current Inventory:")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")

while True:
    print("\nOptions:")
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
        print("Invalid choice, please try again")
