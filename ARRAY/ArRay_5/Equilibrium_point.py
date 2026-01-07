def equilibrium_indices_bruteforce(a):
    ei = []
    for b in range(len(a)):
        left_sum = sum(a[:b])
        right_sum = sum(a[b+1:])
    
        if left_sum == right_sum:
            ei.append(b)
    return ei

arr1 = [1, 2, 3, 4, 3, 2, 1, 0]
arr2 = [2, 3, -1, 8, 4]
arr3 = [1, 2, 3]
arr4 = [0, 0, 0, 0, 0]

print(equilibrium_indices_bruteforce(a = arr1))
print(equilibrium_indices_bruteforce(a = arr2))
print(equilibrium_indices_bruteforce(a = arr3))
print(equilibrium_indices_bruteforce(a = arr4))