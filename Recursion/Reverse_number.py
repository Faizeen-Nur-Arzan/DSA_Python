def reverse_number(num, rev):
    if num == 0:
        return rev
    last_digit = num % 10
    rev = rev * 10 + last_digit
    return reverse_number(num // 10 , rev)

print(reverse_number(123, 0))