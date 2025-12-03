def print_1_to_n(n, num):
    """uses tail recursion to print n to num"""
    if n > num:
        return
    print(n)
    print_1_to_n(n + 1, num)

print_1_to_n(1, 50)