"""
B+ TREE FOR ABSOLUTE BEGINNERS
============================

What is a B+ Tree?

A B+ Tree is a sorted "tree" data structure used by databases to find
data fast. Think of it like a book:

* INTERNAL nodes are like the book's index / signposts. They only say
  "keys smaller than 10 go left, 10 and above go right".
* LEAF nodes are the actual pages. They hold ALL the real keys + values.
* Leaves are chained together like a linked list, so once you find one
  key you can walk right and read the next keys in order (range search).

Key rule: each node can hold at most `max_keys` keys. When a node gets
too full, it SPLITS into two nodes and the middle key is pushed up to
the parent. That is the whole trick.

This file supports: insert, search, range search, and printing.
(Delete is left out on purpose to keep it simple.)
"""


class Node:
    """One box in the tree. It is either a leaf or an internal node."""

    def __init__(self, is_leaf=False):
        self.is_leaf = is_leaf  # True = holds real data, False = signpost only
        self.keys = []          # sorted list of keys, e.g. [10, 20, 30]
        self.children = []      # internal node: child Nodes
                                # leaf node: the VALUES that match each key
        self.next = None        # leaf only: link to the next leaf on the right


class BPlusTree:
    def __init__(self, max_keys=3):
        # max_keys = how many keys a node may hold before it must split.
        # Small number (3) makes splits happen quickly, which is great
        # for learning. Real databases use hundreds.
        if max_keys < 2:
            raise ValueError('max_keys must be at least 2')
        self.max_keys = max_keys
        self.root = Node(is_leaf=True)  # tree starts as one empty leaf

    # -------------------------------------------------------------
    # SEARCH
    # -------------------------------------------------------------
    def _find_leaf(self, key):
        """Walk from the root down to the leaf where `key` belongs."""
        node = self.root
        while not node.is_leaf:
            # Find which child to go into: the first position where
            # key < keys[i]. If none, go to the last (rightmost) child.
            i = 0
            while i < len(node.keys) and key >= node.keys[i]:
                i += 1
            node = node.children[i]
        return node

    def search(self, key):
        """Return the value stored for `key`, or None if not found."""
        leaf = self._find_leaf(key)
        for i in range(len(leaf.keys)):
            if leaf.keys[i] == key:
                return leaf.children[i]  # in a leaf, children = values
        return None

    def range_search(self, low, high):
        """Return all (key, value) pairs with low <= key <= high."""
        results = []
        leaf = self._find_leaf(low)        # start at the leaf containing 'low'
        while leaf is not None:
            for i in range(len(leaf.keys)):
                if leaf.keys[i] > high:
                    return results         # passed the end, stop
                if leaf.keys[i] >= low:
                    results.append((leaf.keys[i], leaf.children[i]))
            leaf = leaf.next               # hop to the next leaf on the right
        return results

    # -------------------------------------------------------------
    # INSERT
    # -------------------------------------------------------------
    def insert(self, key, value):
        """Add a key/value pair. If the key exists, its value is replaced."""
        split_result = self._insert(self.root, key, value)

        # If the ROOT split, the tree must grow taller by one level:
        # make a brand-new root that points to the two halves.
        if split_result is not None:
            promoted_key, new_right_node = split_result
            new_root = Node(is_leaf=False)
            new_root.keys = [promoted_key]
            new_root.children = [self.root, new_right_node]
            self.root = new_root

    def _insert(self, node, key, value):
        """
        Insert into `node` (recursively).
        Returns None if no split happened.
        Returns (promoted_key, new_right_node) if `node` had to split,
        so the parent can add them.
        """
        # --------- CASE 1: we are at a leaf, do the real insert ---------
        if node.is_leaf:
            # Find the sorted position for the new key.
            i = 0
            while i < len(node.keys) and node.keys[i] < key:
                i += 1

            # Key already exists? Just update its value.
            if i < len(node.keys) and node.keys[i] == key:
                node.children[i] = value
                return None

            node.keys.insert(i, key)
            node.children.insert(i, value)

            # Too full? Split the leaf!
            if len(node.keys) > self.max_keys:
                return self._split_leaf(node)
            return None

        # --------- CASE 2: internal node, pass the work down ---------
        i = 0
        while i < len(node.keys) and key >= node.keys[i]:
            i += 1
        child = node.children[i]

        split_result = self._insert(child, key, value)

        # The child split, so we must add its new sibling to ourselves.
        if split_result is not None:
            promoted_key, new_right_node = split_result
            node.keys.insert(i, promoted_key)
            node.children.insert(i + 1, new_right_node)

            # Now WE might be too full. Split ourselves if so.
            if len(node.keys) > self.max_keys:
                return self._split_internal(node)
        return None

    def _split_leaf(self, leaf):
        """Cut a full leaf in half. Right half becomes a new leaf."""
        mid = len(leaf.keys) // 2
        new_leaf = Node(is_leaf=True)

        # Right half moves to the new leaf.
        new_leaf.keys = leaf.keys[mid:]
        new_leaf.children = leaf.children[mid:]
        # Left half stays in the old leaf.
        leaf.keys = leaf.keys[:mid]
        leaf.children = leaf.children[:mid]

        # Keep the leaf chain intact: leaf -> new_leaf -> (old next)
        new_leaf.next = leaf.next
        leaf.next = new_leaf

        # For LEAVES, the promoted key is COPIED up (it also stays in the leaf). This is what makes it a B+ tree: all keys live in leaves.
        return new_leaf.keys[0], new_leaf

    def _split_internal(self, node):
        """Cut a full internal node in half. Middle key moves UP."""
        mid = len(node.keys) // 2
        promoted_key = node.keys[mid]
        new_node = Node(is_leaf=False)

        # Keys after the middle go right. Children after the middle go right.
        new_node.keys = node.keys[mid + 1:]
        new_node.children = node.children[mid + 1:]
        # Left side keeps keys before the middle.
        node.keys = node.keys[:mid]
        node.children = node.children[:mid + 1]

        # For INTERNAL nodes the promoted key is MOVED up (removed here),
        # unlike leaves where it is copied.
        return promoted_key, new_node

    # -------------------------------------------------------------
    # PRINTING (to see what the tree looks like)
    # -------------------------------------------------------------
    def print_tree(self):
        """Print the tree level by level, top to bottom."""
        level = [self.root]
        depth = 0
        while level:
            print(f"Level {depth}: ", end="")
            print(" | ".join(str(n.keys) for n in level))
            next_level = []
            for n in level:
                if not n.is_leaf:
                    next_level.extend(n.children)
            level = next_level
            depth += 1

    def print_leaves(self):
        """Print all leaves left to right by following the 'next' chain."""
        node = self.root
        while not node.is_leaf:      # go all the way down the left edge
            node = node.children[0]
        parts = []
        while node is not None:
            parts.append(str(node.keys))
            node = node.next
        print(" -> ".join(parts))


if __name__ == "__main__":
    tree = BPlusTree(max_keys=3)

    # Insert keys in a scrambled order. Values are just strings here.
    for k in [ 10, 20, 5, 6, 12, 30, 7, 17, 25, 1, 40, 15]:
        tree.insert(k, f"value_{k}")

    print("--- Tree structure (top to bottom) ---")
    tree.print_tree()

    print("\n--- Leaves chained left to right ---")
    tree.print_leaves()

    print("\n--- Search ---")
    print("search(12) ->", tree.search(12))
    print("search(99) ->", tree.search(99))   # not in the tree -> None

    print("\n--- Range search 6..20 ---")
    print(tree.range_search(6, 20))

    print("\n--- Update existing key ---")
    tree.insert(12, "new_value_12")
    print("search(12) ->", tree.search(12))

    # ---- Self-check: leaf chain must be sorted and complete ----
    node = tree.root
    while not node.is_leaf:
        node = node.children[0]
    all_keys = []
    while node:
        all_keys.extend(node.keys)
        node = node.next
    assert all_keys == sorted(all_keys), "keys are not sorted!"
    assert len(all_keys) == 12, "some keys were lost!"
    print("\nSelf-check passed: all 12 keys present and sorted.")