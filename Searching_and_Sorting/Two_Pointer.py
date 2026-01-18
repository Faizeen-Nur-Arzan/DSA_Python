"""Using Two-Pointer Method find the two elements from a given array whose sum is equal to the given value"""

def two_pointer_method(arr, sUm):
    size = len(arr)
    left = 0
    right = size-1

    while (left < right):
        if arr[left] + arr[right] == sUm:
            return arr[left], arr[right]
        elif arr[left] + arr[right] < sUm:
            left += 1
        else:
            right -= 1
    
    return "<>NOWHERE<>"

SuM = int(input("SUUUUUUUUUUUUUUUUUUUUUUUMMMMMMMM?????????\n:"))
list1 = list(map(int, input("Enter arry\n:").split()))
print(two_pointer_method(list1, SuM))