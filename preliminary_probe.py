letion(id='chatcmpl-8vEf12yh2JvxKcjy2X1SMoX02DbXv', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity):
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity

    def remove_item(self, item_name, quantity):
        if item_name in self.items:
            if self.items[item_name] >= quantity:
                self.items[item_name] -= quantity
                if self.items[item_name] == 0:
                    del self.items[item_name]
            else:
                print("Not enough quantity of", item_name)
        else:
            print(item_name, "not found in inventory")

    def display_inventory(self):
        print("Inventory:")
        for item, quantity in self.items.items():
            print(item, ":", quantity)


inventory = Inventory()

while True:
    print("\n1. Add Item")
    print("2. Remove Item")
    print("3. Display Inventory")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        item_name = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        inventory.add_item(item_name, quantity)
    
    elif choice == '2':
        item_name = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        inventory.remove_item(item_name, quantity)
    
    elif choice == '3':
        inventory.display_inventory()
    
    elif choice == '4':
        break
    
    else:
        print("Invalid choice. Please try again.")', role='assistant', function_call=None, tool_calls=None))], created=1708651743, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_cbdb91ce3f', usage=CompletionUsage(completion_tokens=329, prompt_tokens=22, total_tokens=351)