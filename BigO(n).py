def bigO_n(n):
    iteration = 0
    for _ in range(1, n + 1):
        iteration += 1
    print(f"When n is {n} iterations = {iteration}.")

bigO_n(10)
bigO_n(20)
bigO_n(42)
bigO_n(1000000)

print("\nWith every 'n' the time taken and iterations will increase linearly")