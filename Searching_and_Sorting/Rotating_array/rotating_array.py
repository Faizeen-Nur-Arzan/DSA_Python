def ar(a, r):
    n = len(a)
    r = r % n
    return a[r:] + a[:r]

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
r = 2
print(ar(a, r))