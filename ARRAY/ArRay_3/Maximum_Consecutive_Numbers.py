def maximum_consecutive_1s(arr):
    counter = 0
    max_count = 0
    for i in arr:
        if i == 1:
            counter += 1
            if max_count < counter:
                max_count = counter
        else:
            counter = 0
    return max_count

arr = list(eval(input("Enter list\n:")))
print(maximum_consecutive_1s(arr))