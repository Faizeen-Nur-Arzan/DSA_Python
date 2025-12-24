def reverse_in_groups(arr, n):
    """Reverse array in groups of n"""
    length = len(arr)

    for i in range(0, length, n):
        left = i
        right = min(i + n - 1, length - 1)

        # Reverse the current group
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    return arr


# Test cases
arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n1 = 3
print(f"Original array: {arr1}")
print(f"Group size: {n1}")
print(f"Result: {reverse_in_groups(arr1, n1)}")

print("\n---\n")

arr2 = [1, 2, 3, 4, 5, 6, 7, 8]
n2 = 5
print(f"Original array: {arr2}")
print(f"Group size: {n2}")
print(f"Result: {reverse_in_groups(arr2, n2)}")