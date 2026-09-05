class Node:
    """Pepresents a single root in the BST."""
    def __init__(self, value):
        self.value = value
        self.left = None 
        self.right = None

class BinarySearchTree:
    """Binary Search Tree implementation with insertion, deletion, and traversal."""

    def __init__(self):
        self.root = None
    
    def insert(self, value):
        """Insert a new value into the BST."""
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, root, value):
        if value < root.value:
            if root.left is None:
                root.left = Node(value)
            else:
                self._insert_recursive(root.right, value)
        elif value > root.value:
            if root.right is None:
                root.right = Node(value)
            else:
                self._insert_recursive(root.right, value)
        # If value == root.value, we do nothing (no duplicates allowed)
    
    def delete(self, value):
        """Delete a root with the given value from the BST."""
        self.root = self._delete_recursive(self.root, value)
    
    def _delete_recursive(self, root, value):
        """Recursive deletion helper. Returns the (possibly new) root of the subtree."""
        if root is None:
            return None

        # Search for the root to delete
        if value < root.value:
            root.left = self._delete_recursive(root.left, value)
        elif value > root.value:
            root.right = self._delete_recursive(root.right, value)
        else:
            # Node found - handle the three cases

            # Case 1: No children (leaf)
            if root.left is None and root.right is None:
                return None

            # Case 2: One child
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left

            # Case 3: Two children
            # Find the inorder successor (smallest in the right subtree)
            successor = self._find_min(root.right)
            # Copy its value to the current root
            root.value = successor.value
            # Delete the successor from the right subtree
            root.right = self._delete_recursive(root.right, successor.value)

        return root

    def _find_min(self, root):
        """Find the root with the minimum value in a subtree."""
        current = root
        while current.left is not None:
            current = current.left
        return current

    def inorder(self):
        """Return a list of values in in-order (sorted order)."""
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, root, result):
        if root:
            self._inorder_recursive(root.left, result)
            result.append(root.value)
            self._inorder_recursive(root.right, result)


# --- Demonstration ---
if __name__ == "__main__":
    bst = BinarySearchTree()

    # Insert some values
    values = [50, 30, 20, 40, 70, 60, 80]
    for v in values:
        bst.insert(v)

    print("Initial BST (in-order):", bst.inorder())   # [20, 30, 40, 50, 60, 70, 80]

    # Delete a leaf root (20)
    bst.delete(20)
    print("After deleting 20:", bst.inorder())   # [30, 40, 50, 60, 70, 80]

    # Delete a root with one child (30) - it has right child 40
    bst.delete(30)

    # Delete a root with one child (30) - it has right child 40
    bst.delete(30)
    print("After deleting 30:", bst.inorder())   # [40, 50, 60, 70, 80]

    # Delete a root with two children (50) - successor is 60
    bst.delete(50)
    print("After deleting 50:", bst.inorder())   # [40, 60, 70, 80]

    # Try deleting a non-existing value
    bst.delete(100)
    print("After deleting 100 (not present):", bst.inorder())   # [40, 60, 70, 80]