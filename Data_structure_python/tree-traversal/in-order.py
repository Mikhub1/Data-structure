class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to perform inorder traversal
def inorderTraversal(root):
  
    # Base case: if null
    if root is None:
        return 0
      
    # Recur on the left subtree
    inorderTraversal(root.left)
    
    # Visit the current node
    print(root.data, end=" ")
    
    # Recur on the right subtree
    inorderTraversal(root.right)

    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(7)
root.right.right = Node(8)

inorderTraversal(root)