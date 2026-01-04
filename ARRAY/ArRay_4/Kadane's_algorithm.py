def max_subarray_sum(a):
    """Finds the largest subarray sum using Kadane's algorithm"""
    res = a[0]
    maxEnding = a[0]
    for i in range(0, len(a)):
        maxEnding = max(a[i], maxEnding + a[i])
        res = max(res, maxEnding)
    return res

b = [1, 2, 4, 1, -100, 1000, -1000]
c = [2, 3, -8, 7, -1, 2, 3]
print(max_subarray_sum(b))
print(max_subarray_sum(c))