letion(id='chatcmpl-9e5lilcY3p5t5r2wIb1KVQlxQLagO', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='# Inventory Management System

# Initialize an empty inventory dictionary
inventory = {}

# Function to add an item to the inventory
def add_item():
    item_name = input("Enter item name: ")
    item_quantity = int(input("Enter item quantity: "))
    
    if item_name in inventory:
        inventory[item_name] += item_quantity
    else:
        inventory[item_name] = item_quantity
        
    print(f"{item_quantity} {item_name}(s) added to inventory.")

# Function to remove an item from the inventory
def remove_item():
    item_name = input("Enter item name: ")
    item_quantity = int(input("Enter quantity to remove: "))
    
    if item_name in inventory:
        if inventory[item_name] >= item_quantity:
            inventory[item_name] -= item_quantity
            print(f"{item_quantity} {item_name}(s) removed from inventory.")
        else:
            print("Not enough quantity in inventory.")
    else:
        print("Item not found in inventory.")

# Function to display the current inventory
def display_inventory():
    print("Current Inventory:")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")

# Main program loop
while True:
    print("\nInventory Management System:")
    print("1. Add item to inventory")
    print("2. Remove item from inventory")
    print("3. Display current inventory")
    print("4. Exit")
    
    choice = int(input("Enter choice: "))
    
    if choice == 1:
        add_item()
    elif choice == 2:
        remove_item()
    elif choice == 3:
        display_inventory()
    elif choice == 4:
        break
    else:
        print("Invalid choice.")
        
print("Exiting Inventory Management System.")', role='assistant', function_call=None, tool_calls=None))], created=1719342322, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=364, prompt_tokens=20, total_tokens=384)