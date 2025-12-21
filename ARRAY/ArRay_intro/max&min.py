def maximum(a):
    s = len(a)
    if s == 0:
        return None
    c = a[0]
    for b in range(1, s):
        if a[b] > c:
            c = a[b]
    return c

def minimum(d):
    e = len(d)
    if e == 0:
        return None
    f = d[0]
    for g in range(1, e):
        if d[g] < f:
            f = d[g]
    return f

def find_minimum_and_maximum(h):
    print(h)
    print(f"minimum value : {minimum(h)}\nmaximum value : {maximum(h)}")

a1 = [1, 2, 3, 4, 5]
a2 = [89, 45, 47, 67, 89]
a3 = [420, 56, 46, 80, 12]
a4 = [69, 70, 43, 9, 6]
a5 = []

find_minimum_and_maximum(a1)
find_minimum_and_maximum(a2)
find_minimum_and_maximum(a3)
find_minimum_and_maximum(a4)
find_minimum_and_maximum(a5)