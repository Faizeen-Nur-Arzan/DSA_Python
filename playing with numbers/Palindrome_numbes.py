def isNumPalindrome(n):
    or_n = n
    re_n = 0
    while n > 0:
        last_digit = n % 10
        re_n = re_n * 10 + last_digit
        n //= 10
    
    return "Palindrome" if or_n == re_n else "Not Palindrome"

inp = int(input("Enter a number: "))
print(isNumPalindrome(inp))