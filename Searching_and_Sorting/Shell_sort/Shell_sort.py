def shell_sort(arr):
    n = len(arr)
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = arr[i]
            j = i
            while j >= interval and arr[j - interval] > temp:
                arr[j] = arr[j - interval]
                j -= interval
            
            arr[j] = temp
        interval //= 2
    return arr

arr = [9, 8, 3, 7, 5, 6, 4, 1]
print("Sorted Array:")
print(shell_sort(arr))