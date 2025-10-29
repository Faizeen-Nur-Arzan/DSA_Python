def count_0s_1s(n):
    ones = 0
    zeros = 0
    bina = bin(n)[2::]
    while n > 0:
        if n & 1 == 1:
            ones += 1
        else:
            zeros += 1
        n >>= 1
    return f"Binary : {bina}\nZeros : {zeros}\nOnes : {ones}"

print(count_0s_1s(int(input("Enter any number: "))))