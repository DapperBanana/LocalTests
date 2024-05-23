
inventory = {}

def add_item():
    item_name = input("Enter the name of the item: ")
    item_quantity = int(input("Enter the quantity of the item: "))
    inventory[item_name] = item_quantity
    print(f"{item_name} has been added to the inventory.")

def remove_item():
    item_name = input("Enter the name of the item you want to remove: ")
    if item_name in inventory:
        del inventory[item_name]
        print(f"{item_name} has been removed from the inventory.")
    else:
        print("Item not found in inventory.")

def display_inventory():
    print("Inventory:")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")

def main():
    while True:
        print("\nInventory Management System")
        print("1. Add item to inventory")
        print("2. Remove item from inventory")
        print("3. Display inventory")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_item()
        elif choice == 2:
            remove_item()
        elif choice == 3:
            display_inventory()
        elif choice == 4:
            print("Exiting inventory management system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
