# A single node in a binary tree
class Node:
    def __init__(self, data):
        self.data = data   # The value stored
        self.left = None   # Reference to left child
        self.right = None   # Reference to right child

# A tree is just a reference to its root node
class BinaryTree:
    def __init__(self):
        self.root = None   # Empty tree has no root
    
    def inorder(self, node):
        """Left → Node → Right. O(n) time, O(h) space."""
        if node is None:   # Base case: empty tree
            return
        
        self.inorder(node.left)   # 1. Recurse left
        print(node.data, end="=>")   # 2. Visit node
        self.inorder(node.right)   # 3. Recurse right
    
    def preorder(self, node):
        """Node → Left → Right. Great for tree serialization."""
        if node is None:   # Base case: empty tree
            return
        
        print(node.data, end="=>")   # 1. Visit node FIRST
        self.preorder(node.left)   # 2. Recurse left
        self.preorder(node.right)   # 3. Recurse right
    
    def postorder(self, node):
        """Left → Right → Node. Visit children before parent."""
        if node is None:   # Base case: empty tree
            return
        
        self.postorder(node.left)   # 1. Recurse left
        self.postorder(node.right)   # 2. Recurse right
        print(node.data, end="=>")   # 3. Visit node LAST

tree = BinaryTree()

# Root (deg = 0)
tree.root = Node(1)
# Left subtree of root (deg = 1)
tree.root.left = Node(2)
# Left subtree of left subtree of root (deg = 2)
tree.root.left.left = Node(4)
# Right leaf of left subtree of leaf subtree of root (deg = 3)
tree.root.left.left.right = Node(8)
# Right subtree of left subtree of root (deg = 2)
tree.root.left.right = Node(5)
# Right subtree of right subtree of left subtree of root (deg = 3)
tree.root.left.right.right = Node(9)
# Left subtree of right subtree of right subtree of left subtree of root (deg = 4)
tree.root.left.right.right.left = Node(10)
# Left leaf of left subtree of right subtree of right subtree of left subtree of root (deg = 5)
tree.root.left.right.right.left.left = Node(11)
# Right leaf of left subtree of right subtree of right subtree of left subtree of root (deg = 5)
tree.root.left.right.right.left.right = Node(12)

# Right subtree of root (deg = 1)
tree.root.right = Node(3)
# Left leaf of right subtree of root (deg = 2)
tree.root.right.left = Node(6)
# Right leaf of right subtree of root (deg = 2)
tree.root.right.right = Node(7)

print("Inorder Traversal:")
tree.inorder(tree.root)
print()
print("Preorder Traversal:")
tree.preorder(tree.root)
print()
print("Postorder Traversal:")
tree.postorder(tree.root)
print()