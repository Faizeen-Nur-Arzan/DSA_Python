# This function does the clever MERGING part
def merge(left, right):
    result = []    # Our new, sorted pile goes here
    i = 0   # Pointer for the left pile
    j = 0   # Pointer for the right pile

    # Keep comparing the first cards of each pile until one pile is empty
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:    # If the left card is smaller...
            result.append(left[i])    # ...take it fro the left pile
            i += 1
        else:    # Otherwise, the right card is smaller...
            result.append(right[j])    # ...take it from the right pile
            j += 1
    
    # If the left pile still has cards, just add them all (they're already sorted!)
    while i < len(left):
        result.append(left[i])
        i += 1
    
    # If the right pile still has cards, just add them all (they're already sorted!)
    while j < len(right):
        result.append(right[j])
        j += 1
    
    return result    # Give back the fully merged and sorted pile!

def merge_sort(whole_list):
    if len(whole_list) <= 1:
        return whole_list
    
    mid = len(whole_list) // 2
    left_half = whole_list[:mid]
    right_half = whole_list[mid:]

    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    return merge(sorted_left, sorted_right)

unsorted_list = [8, 3, 9, 1, 5, 2]
sorted_list = merge_sort(unsorted_list)
print(f"Original\n: {unsorted_list}")
print(f"Sorted\n: {sorted_list}")