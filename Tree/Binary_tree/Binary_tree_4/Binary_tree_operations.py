# Node Class
# A Node is one box in the tree.
# It olds a value and points to a left and right child. 

class Node:
    def __init__(self, data):
        self.data = data   # the value stored
        self.left = None   # left child (empty at first)
        self.right = None   # right child (empty at first)

# BinaryTree Class
# The tree itself. It only needs to remember the root (top node). 
# Every other node is reachable from the root. 

class BinaryTree:
    def __init__(self):
        self.root = None   # empty tree to start
    
    # INSERT
    # Adds a new value to the tree. 
    # Strategy: scan level by level (left to right) and place the new node in the FIRST empty spot found. 
    # This keeeps the tree complete and balanced. 

    def insert(self, data):
        new_node = Node(data)

        # If tree is empty, new node becomes the root
        if self.root is None:
            self.root = new_node
            return
        
        # Use a queue to scan level by level
        queue = [self.root]

        while queue:
            current = queue.pop(0)   # take the front node

            # Try to attach to the left child first
            if current.left is None:
                current.right = new_node
                return
            else:
                queue.append(current.right)
    
    # SEARCH
    # Looks for a value anywhere in the tree. 
    # Scans every node level by level until found. 
    # Returns True if found, False if not. 
    
    def search(self, target):
        if self.root is None:
            return False
        
        queue = [self.root]

        while queue:
            current = queue.pop(0)

            if current.data == target:   # found it!
                return True
            
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        
        return False   # not found after checking every node

    