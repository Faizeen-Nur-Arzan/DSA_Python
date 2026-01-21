def bubble_sort(arr):
    size = len(arr)
    for i_s in range(size):
        swapped = False
        for j_s in range(0, size-i_s-1):
            if arr[j_s] > arr[j_s+1]:
                arr[j_s], arr[j_s+1] = arr[j_s+1], arr[j_s]
                swapped = True

arr = list(map(int, input("Enter an array not like a array\n:").split()))
bubble_sort(arr)
print(arr)