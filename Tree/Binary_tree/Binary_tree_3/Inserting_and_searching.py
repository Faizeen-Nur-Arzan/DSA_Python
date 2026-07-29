class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    # INSERT
    # Adds a new value to the tree.
    # Strategy: scan level by level (left to right) and place the new node in the FIRST empty spot found.
    # This keeps the tree complete and balanced.

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
                current.left = new_node
                return
            else:
                queue.append(current.left)
            
            # Then try the right child
            if current.right is None:
                current.right = new_node
                return
            else:
                queue.append(current.right)
        
        # SEARCH
        # Looks for a value anywhere in the tree.
        # Scans every node level by level until found.
        # Return True if found, False if not.

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
        
        # DISPLAY
        # Prints the tree level by level so you can see its shape.

        def display(self):
            if self.root is None:
                print("Tree is empty.")
                return
            
            queue = [self.root]
            level = 1

            while queue:
                level_size = len(queue)
                print(f"  Level {level} : ", end="")

                for _ in range(level_size):
                    node = queue.pop(0)