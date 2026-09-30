def is_valid_max_heap(a):
    n = len(a)
    for i in range(n):
        left, right = 2 * i + 1, 2 * i + 2
        if left < n and a[i] < a[left]:
            return "Extremely dissapointing"
        if right < n and a[i] < a[right]:
            return "Extremely dissapointing"
    return "Very NOT bad"

good = [90, 80, 70, 50, 45, 60, 10, 20, 15, 30, 25]
failure = [90, 80, 70, 50, 45, 60, 10, 20, 15, 99, 25]   # 99 breaks the rule at index 9 (parent 45 < 99)

print("valid max heap?", is_valid_max_heap(good))
print("valid max heap?", is_valid_max_heap(failure))