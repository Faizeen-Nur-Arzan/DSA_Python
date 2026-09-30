class BTreeNode:
    def __init__(self, is_leaf=True):
        self.keys = []   # sorted list of keys
        self.children = []   # pointers to child nodes
        self.is_leaf = is_leaf   # True if no children


class BTree:
    def __init__(self, t=2):
        self.root = BTreeNode(is_leaf=True)
        self.t = t  # minimum degree

    # --- SEARCH ---
    def search(self, key, node=None):
        if node is None:
            node = self.root

        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1

        if i < len(node.keys) and node.keys[i] == key:
            return True

        if node.is_leaf:
            return False

        return self.search(key, node.children[i])

    # --- INSERT ---

    def insert(self, key):
        root = self.root
        if len(root.keys) == 2 * self.t - 1:
            # root is full -> split, create a new root
            new_root = BTreeNode(is_leaf=False)
            new_root.children.append(root)
            self._split_child(new_root, 0)
            self.root = new_root

        self._insert_non_full(self.root, key)

    def _insert_non_full(self, node, key):
        i = len(node.keys) - 1

        if node.is_leaf:
            node.keys.append(None)
            while i >= 0 and key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = key
        else:
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1

            if len(node.children[i].keys) == 2 * self.t - 1:
                self._split_child(node, i)
                if key > node.keys[i]:
                    i += 1

            self._insert_non_full(node.children[i], key)

    def _split_child(self, parent, i):
        t = self.t
        y = parent.children[i]
        z = BTreeNode(is_leaf=y.is_leaf)

        z.keys = y.keys[t:]
        middle = y.keys[t - 1]
        y.keys = y.keys[:t - 1]

        if not y.is_leaf:
            z.children = y.children[t:]
            y.children = y.children[:t]

        parent.children.insert(i + 1, z)
        parent.keys.insert(i, middle)

    # --- DEBUG: print the tree ---
    def print_tree(self, node=None, level=0):
        if node is None:
            node = self.root

        print("  " * level + str(node.keys))

        for child in node.children:
            self.print_tree(child, level + 1)


# --- TRY IT ---
if __name__ == "__main__":
    tree = BTree(t=2)   # each node holds 1-3 keys

    for num in [10, 20, 5, 6, 12, 30, 7, 17, 3, 25]:
        tree.insert(num)

    print("Tree structure:")
    tree.print_tree()

    print("Is 17 in tree?", tree.search(17))
    print("Is 99 in tree?", tree.search(99))