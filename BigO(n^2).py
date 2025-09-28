def bigO_n2(n):
    iteration = 0
    for _ in range(1, n + 1):
        for _ in range(1, n + 1):
            iteration += 1
    print(f"\nWhen n is {n} iteration = {iteration}")
bigO_n2(5)
bigO_n2(40)
bigO_n2(300)

print("\nWith every 'n' the iteration time taken = n^2")
print("Time Complexity is: O(n^2)")