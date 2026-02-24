def unite_arrays(a1, a2):
    i, j = 0, 0
    ua = []

    while i < len(a1) and j < len(a2):
        while i > 0 and i < len(a1) and a1[i] == a1[i-1]:
            i += 1
        while j > 0 and j < len(a2) and a2[j] == a2[j-1]:
            j += 1
        if i >= len(a1) or j >= len(a2):
            break
        if a1[i] < a2[j]:
            ua.append(a1[i])
            i += 1
        if a1[i] > a2[j]:
            ua.append(a2[j])
            j += 1
        else:
            ua.append(a1[i])
            i += 1
            j += 1
    
    while i < len(a1):
        if i == 0 or a1[i] != a1[i-1]:
            ua.append(a1[i])
        i += 1
    
    while j < len(a2):
        if j == 0 or a2[j] != a2[j-1]:
            ua.append(a2[j])
        j += 1
    
    return ua

a_ = [1, 3, 4, 5, 7]
a__ = [2, 3, 5, 6]
r_ = unite_arrays(a_, a__)
print(f"Array 1\n: {a_}")
print(f"Array 2\n: {a__}")
print(f"Result\n: {r_}")
print(f"Time complexity is : 0(m+n) where m is the size of the frst array and n is the second.")