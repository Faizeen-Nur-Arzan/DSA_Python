def print_n_to_1(n, num):
    """uses head recursion to print num to n"""
    if n > num:
        return
    print_n_to_1(n + 1, num)
    print(n)

print_n_to_1(1, 50)