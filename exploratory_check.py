
# Text-based inventory management system

inventory = {}

def add_item(item_name, quantity):
    if item_name in inventory:
        inventory[item_name] += quantity
    else:
        inventory[item_name] = quantity
    print(f"Added {quantity} {item_name} to inventory.")

def remove_item(item_name, quantity):
    if item_name in inventory:
        if inventory[item_name] >= quantity:
            inventory[item_name] -= quantity
            print(f"Removed {quantity} {item_name} from inventory.")
        else:
            print(f"Not enough {item_name} in inventory.")
    else:
        print(f"{item_name} not found in inventory.")

def check_inventory():
    print("\nCurrent Inventory:")
    for item_name, quantity in inventory.items():
        print(f"{item_name}: {quantity}")
    print("")

def main():
    while True:
        print("1. Add item to inventory")
        print("2. Remove item from inventory")
        print("3. Check inventory")
        print("4. Exit")
        
        choice = input("\nEnter choice: ")
        
        if choice == "1":
            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            add_item(item_name, quantity)
        elif choice == "2":
            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            remove_item(item_name, quantity)
        elif choice == "3":
            check_inventory()
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
