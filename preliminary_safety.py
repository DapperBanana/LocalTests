
inventory = {}

def add_item():
    item_name = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    inventory[item_name] = quantity
    print(f"{quantity} {item_name} added to inventory.")

def remove_item():
    item_name = input("Enter item name: ")
    if item_name in inventory:
        del inventory[item_name]
        print(f"{item_name} removed from inventory.")
    else:
        print("Item not found in inventory.")

def display_inventory():
    print("Current Inventory:")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")

def main():
    while True:
        print("\n1. Add Item\n2. Remove Item\n3. Display Inventory\n4. Exit")
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

if __name__ == "__main__":
    main()
