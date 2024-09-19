
inventory = {}

def add_item():
    name = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    inventory[name] = inventory.get(name, 0) + quantity
    print(f"{quantity} {name} added to inventory.")

def remove_item():
    name = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    if name in inventory and inventory[name] >= quantity:
        inventory[name] -= quantity
        print(f"{quantity} {name} removed from inventory.")
    else:
        print("Item not found or quantity exceeds inventory.")

def display_inventory():
    print("Inventory:")
    for item, count in inventory.items():
        print(f"{item}: {count}")

def main():
    while True:
        print("\n1. Add Item\n2. Remove Item\n3. Display Inventory\n4. Exit")
        choice = input("Enter choice: ")
        
        if choice == "1":
            add_item()
        elif choice == "2":
            remove_item()
        elif choice == "3":
            display_inventory()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
