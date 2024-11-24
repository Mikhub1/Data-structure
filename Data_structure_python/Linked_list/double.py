class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return f"Element {key} found in the list."
            current = current.next
        return f"Element {key} not in the list."

# Example usage
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.append(5)
dll.display()  # Output: 1 2 3 4 5

# Search for an element
print(dll.search(3))  # Output: Element 3 found in the list.
print(dll.search(6))  # Output: Element 6 not in the list.
