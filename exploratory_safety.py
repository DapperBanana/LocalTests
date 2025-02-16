
def display_menu():
    print("\nMENU")
    print("1. Add item to inventory")
    print("2. Remove item from inventory")
    print("3. View inventory")
    print("4. Exit")
    
def add_item(inventory):
    item = input("\nEnter item to add: ")
    quantity = int(input("Enter quantity: "))
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity
    print("Item added to inventory")
    
def remove_item(inventory):
    item = input("\nEnter item to remove: ")
    if item in inventory:
        quantity = int(input("Enter quantity to remove: "))
        if quantity >= inventory[item]:
            del inventory[item]
        else:
            inventory[item] -= quantity
        print("Item removed from inventory")
    else:
        print("Item not found in inventory")
    
def view_inventory(inventory):
    print("\nINVENTORY")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")
    
def main():
    inventory = {}
    
    while True:
        display_menu()
        choice = input("\nEnter choice: ")
        
        if choice == '1':
            add_item(inventory)
        elif choice == '2':
            remove_item(inventory)
        elif choice == '3':
            view_inventory(inventory)
        elif choice == '4':
            print("Exiting program")
            break
        else:
            print("Invalid choice, please try again")
    
if __name__ == "__main__":
    main()
