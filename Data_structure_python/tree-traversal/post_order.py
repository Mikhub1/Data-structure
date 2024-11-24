class Node:
    # Constructor to create a new node
    def __init__(self, data):
        # Assign data to this node
        self.data = data
        self.left = None
        self.right = None

# Function to perform postorder traversal
def postorderTraversal(node):
    # Base case: if the current node is null, return
    if node is None:
        return
    # Recur on the left subtree
    postorderTraversal(node.left)
    # Recur on the right subtree
    postorderTraversal(node.right)
    # Visit the current node
    print(node.data, end=' ')

# Main function
def main():
    # Creating the tree nodes
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    # Perform postorder traversal
    print("Postorder traversal: ", end='')
    postorderTraversal(root)
    print()

# Run the main function
if __name__ == "__main__":
    main()