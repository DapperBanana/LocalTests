
# Inventory management system

inventory = {} # empty dictionary to store the items

def add_item():
    name = input("Enter the name of the item: ")
    quantity = int(input("Enter the quantity of the item: "))
    inventory[name] = quantity
    print("Item added to inventory.")

def remove_item():
    name = input("Enter the name of the item to remove: ")
    if name in inventory:
        del inventory[name]
        print("Item removed from inventory.")
    else:
        print("Item not found in inventory.")

def display_inventory():
    print("\nCurrent inventory:")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")

def main():
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
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
