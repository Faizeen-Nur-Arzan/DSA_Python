def find_factors(num):
    factors = []
    for cn in range(1, num+1):
        if num % cn == 0:
            factors.append(cn)
    return factors

num = int(input("Enter a number: "))
print(find_factors(num))