# Python program to implement
# inorder traversal of BST

# Given Node node
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Function to create a new BST node
def newNode(item):
    node = Node(item)
    node.key = item
    node.left = None
    node.right = None
    return node

# Function to insert a new node with
# given key in BST
def insert(node, left):
    # If the tree is empty, return a new node
    if node is None:
        return newNode(key)
    
    # Otherwise, recur down the tree
    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)
    # Return the node pointer
    return node

# Function to do inorder traversal of BST
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

def preorder(root):
    if root:
        print(root.key, end=" ")
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.key, end=" ")

# Driver Code
if __name__ == "__main__":

    # Let us create following BST
    #
    #          50
    #        /    \
    #       30     70
    #      /  \   /  \
    #     20  40 60  80
    #
    root = None

    # Creating the BST
    root = insert(root, 50)
    insert(root, 30)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)

    # Function Call
    inorder(root)
    print()
    print("Pre order traversal of Binary Search Tree:")
    preorder(root)
    print()
    print("Post order traversal of Binary Search Tree:")
    postorder(root)