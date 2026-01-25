def selection_sort_ascending(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr

def selection_sort_descending(arr):
    n = len(arr)
    for i in range(n - 1):
        max_index = i
        for j in range(i + 1, n):
            if arr[j] > arr[max_index]:
                max_index = j
        arr[max_index], arr[i] = arr[i], arr[max_index]
    return arr
arr = list(map(int, input("Enter list\n:").split()))

print(selection_sort_ascending(arr=arr))
des = selection_sort_descending(arr=arr)[0]
print(selection_sort_descending(arr=arr))
print(des)