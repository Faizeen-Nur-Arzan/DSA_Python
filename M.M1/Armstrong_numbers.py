def armstrong_num_check(num):
    no_of_digits = len(str(num))
    sum = 0
    for digit in str(num):
        sum = sum + int(digit)**no_of_digits
    if sum == num:
        return True
    else:
        return False

n = int(input("Enter a Number: "))
print(armstrong_num_check(n))