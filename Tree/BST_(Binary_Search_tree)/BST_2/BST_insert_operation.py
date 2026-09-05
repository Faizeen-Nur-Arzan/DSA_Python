class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def newNode(key):
    node = Node(key)
    return node

def insert(node, value):
    if node is None:
        return newNode(value)
    
    if node.key < value:
        node.right = insert(node.right, value)
    elif node.key > value:
        node.left = insert(node.left, value)
    return node

def search(root, target):
    if root:
        if target in inorder(root):
            return True
    return False

def inorder(root):
    if root:
        #inorder(root.left)
        #print(root.key, end="⇆⇄")
        #inorder(root.right)
        return [inorder(root.left), root.key, inorder(root.right)]

if __name__ == "__main__":
    root = None

    root = insert(root, 50)
    insert(root, 10)
    insert(root, 30)
    insert(root, 40)
    insert(root, 100)
    insert(root, 70)
    insert(root, 20)
    insert(root, 60)
    insert(root, 80)
    insert(root, 90)

    print(inorder(root))
    print(search(root, 20))