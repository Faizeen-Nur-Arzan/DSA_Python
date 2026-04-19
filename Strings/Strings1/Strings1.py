n1 = "28905679"
n2 = "16593207"
n3 = "90425861"

def reverse_naive_approach(s):
    r = ""
    l = len(s)

    for i in range(l-1, -1, -1):
        r += s[i]

    return r

def reverse_swapping(s):
    l = len(s)
    s = list(s)

    for i in range(l//2):
        s[i], s[l-i-1] = s[l-i-1], s[i]
    
    return "".join(s)

def reverse_slicing(s):
    return s[::-1]

print(reverse_naive_approach(n1))
print(reverse_swapping(n2))
print(reverse_slicing(n3))