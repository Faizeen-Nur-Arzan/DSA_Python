def recursive_sum(arr, index = 0):
    """
    Args:
        arr: List of numbers
        index: Current index (default: 0)
    Returns:
        Sum of all elements in the array
        """
    # Base case: if we've reached the end of the array
    if index == len(arr):
        return 0
    
    # Recursive case: current element + sum of the rest
    return arr[index] + recursive_sum(arr, index + 1)


test_arrays = [
        [1, 2, 3, 4, 5],
        [10],
        [],
        [2.5, 3.5, 1.0],
        [-1, 0, 1]
    ]
for arr in test_arrays:
    sum = recursive_sum(arr)
    print(f"Array: {arr}")
    print(f"Sum with index: {sum}")
    print()