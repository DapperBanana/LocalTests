
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' -> ')
            current_node = current_node.next
        print('None')

    def delete(self, data):
        current_node = self.head
        if current_node and current_node.data == data:
            self.head = current_node.next
            current_node = None
            return

        prev = None
        while current_node and current_node.data != data:
            prev = current_node
            current_node = current_node.next

        if current_node is None:
            print(f'{data} not found in the list')
            return
        prev.next = current_node.next
        current_node = None

# Create a linked list
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)

# Print the linked list
ll.print_list()

# Delete a node from the linked list
ll.delete(2)
ll.print_list()
