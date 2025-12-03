def factorialRecur(n):
    if n <= 0:
        return 1
    return n * factorialRecur(n - 1)
print(factorialRecur(5))