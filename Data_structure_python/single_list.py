class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        tops = self.head
        while tops.next:
            tops = tops.next
        tops.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def search(self, key):
        current = self.head
        if current == key:
            return f"Element {key} found in the list."
        current = current.next
        return self.search(key)
        #    if current.data == key:
        #        return f"Element {key} found in the list."
        #    current = current.next
        #return f"Element {key} not in the list."


# Example usage
sll = SingleLinkedList()
sll.append(1)
sll.append(2)
sll.append(3)
sll.append(4)
sll.append(5)
sll.display()

print(sll.search(3))  # Output: Element 3 found in the list.
print(sll.search(6)) 
