def is_rotated_and_sorted(arr):
    n = len(arr)
    count = 0

    for i in range(1, n):
        if arr[i-1] > arr[i]:
            count += 1
    
    if arr[n-1] > arr[0]:
        count +=1

    return count <= 1

if __name__ == "__main__":
    test_arrays = [
        [3, 4, 5, 1, 2],
        [1, 2, 3, 4, 5],
        [5, 1, 2, 3, 4],
        [1, 3, 2, 4, 5],
        [2, 1, 3, 4, 5]
    ]

    for arr in test_arrays:
        result = is_rotated_and_sorted(arr)
        print(f"Array {arr} -> Is rotated and sorted? {result}")