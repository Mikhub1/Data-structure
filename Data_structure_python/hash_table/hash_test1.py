class Node: 
    def __init__(self, key, value): 
        self.key = key 
        self.value = value 
        self.next = None
  
  
class HashTable: 
    def __init__(self, capacity): 
        self.capacity = capacity 
        self.size = 0
        self.table = [None] * capacity 
  
    def _hash(self, key): 
        # Calculate the index by hashing the key and taking modulo
        return hash(key) % self.capacity 
  
    def insert(self, key, value): 
        # Get the index where the key-value pair should go
        index = self._hash(key) 
  
        # If the bucket is empty, insert the new node directly
        if self.table[index] is None: 
            self.table[index] = Node(key, value) 
            self.size += 1
        else: 
            # Traverse the linked list at the bucket index
            current = self.table[index] 
            while current: 
                # If the key already exists, update the value
                if current.key == key: 
                    current.value = value 
                    return
                # If at the end of the chain, break to add a new node
                if current.next is None:
                    break
                current = current.next
            # Add a new node at the end of the chain
            current.next = Node(key, value) 
            self.size += 1
  
    def search(self, key): 
        # Get the index where the key might exist
        index = self._hash(key) 
  
        # Traverse the linked list at the bucket index
        current = self.table[index] 
        while current: 
            # Return the value if the key is found
            if current.key == key: 
                return current.value 
            current = current.next
  
        # If the key is not found, raise a KeyError
        raise KeyError(f"Key '{key}' not found.") 
  
    def remove(self, key): 
        # Get the index where the key might exist
        index = self._hash(key) 
  
        # Use two pointers to traverse the chain and remove the key
        previous = None
        current = self.table[index] 
  
        while current: 
            if current.key == key: 
                # If the node to be removed is not the head
                if previous: 
                    previous.next = current.next
                else: 
                    # If the node to be removed is the head
                    self.table[index] = current.next
                self.size -= 1
                return
            previous = current 
            current = current.next
  
        # If the key is not found, raise a KeyError
        raise KeyError(f"Key '{key}' not found.") 
  
    def __len__(self): 
        # Return the total number of key-value pairs
        return self.size 
  
    def __contains__(self, key): 
        # Check if a key exists in the hash table
        try: 
            self.search(key) 
            return True
        except KeyError: 
            return False
  
  
# Driver code 
if __name__ == '__main__': 
    # Create a hash table with a capacity of 5
    ht = HashTable(5) 
  
    # Add some key-value pairs to the hash table
    ht.insert("apple", 3) 
    ht.insert("banana", 2) 
    ht.insert("cherry", 5) 
    ht.insert("cherry", 6)  # Updates "cherry" to 6
  
    # Check if the hash table contains a key
    print("apple" in ht)  # True 
    print("durian" in ht)  # False 
  
    # Get the value for a key
    print(ht.search("banana"))  # 2 
  
    # Update the value for a key
    ht.insert("banana", 4) 
    print(ht.search("banana"))  # 4 
  
    # Remove a key
    ht.remove("apple") 
    # Check the size of the hash table
    print(len(ht))  # 3 





#current = current.next
#This line moves the pointer current to the next node in the chain.
#It ensures that the traversal continues through the linked list until:
#Either the key is found, or
#The end of the chain is reached (when current.next is None).