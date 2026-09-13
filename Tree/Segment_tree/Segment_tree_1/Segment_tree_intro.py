# For an input array of size n, a list of size 4 * n is always big enough.

def build_segment_tree(arr, tree, node, segment_start, segment_end):
    """
    Fill in one node of the segment tree, and (through recursion) all of its
    descendants too.

    arr       -> the original array of numbers, e.g. [1, 3, 5, 7, 9, 11]
    tree      -> the list we are filling in (starts as all zeros)
    node      -> which slot inside `tree` we are working on right now
    segment_start -> leftmost index of `arr` that this node is in charge of
    segment_end   -> rightmost index of `arr` that this node is in charge of
    """

    # BASE CASE: this node is in charge of ONE element only.
    # There is nothing to add together, so just copy that element in.
    if segment_start == segment_end:
        tree[node] = arr[segment_start]
        return

    # Otherwise, split the range in half and let the two children do the work.
    mid = (segment_start + segment_end) // 2   # midpoint of the range
    left_child = 2 * node + 1   # left child's slot in `tree`
    right_child = 2 * node + 2   # right child's slot in `tree`

    # Ask the left child to take care of [segment_start .. mid]
    build_segment_tree(arr, tree, left_child, segment_start, mid)

    # Ask the right child to take care of [mid + 1 .. segment_end]
    build_segment_tree(arr, tree, right_child, mid + 1, segment_end)

    # Once both children know their sums, this node's sum is simply the
    # sum of its two children. (This is the "combining" step.)
    tree[node] = tree[left_child] + tree[right_child]

# --- Try it out ---
arr = [1, 3, 5, 7, 9, 11]   # the original array (6 numbers)
n = len(arr)   # n = 6
tree = [0] * (4 * n)   # room for the tree; all zeros to start

# Build the whole tree. Start at slot 0 (the root), which is in charge of
# the whole array from index 0 to index n - 1.
build_segment_tree(arr, tree, 0, 0, n - 1)

print(tree)   # The root now holds the sum of the whole array: 36