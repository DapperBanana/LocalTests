
inventory = {}

def add_item(item, quantity):
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity

def remove_item(item, quantity):
    if item in inventory:
        if inventory[item] >= quantity:
            inventory[item] -= quantity
        else:
            print("Error: Not enough quantity of {} in inventory.".format(item))
    else:
        print("Error: {} not found in inventory.".format(item))

def display_inventory():
    print("Inventory:")
    for item, quantity in inventory.items():
        print("{}: {}".format(item, quantity))

def main():
    while True:
        print("1. Add item to inventory")
        print("2. Remove item from inventory")
        print("3. Display inventory")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            add_item(item, quantity)
        elif choice == '2':
            item = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            remove_item(item, quantity)
        elif choice == '3':
            display_inventory()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
