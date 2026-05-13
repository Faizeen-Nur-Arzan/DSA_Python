def build_lps_array(pattern):
    m = len(pattern)
    lps = [0] * m
    length = 0  # length of previous longest prefix suffix
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            # Characters math, extend the lps
            length += 1
            lps[i] = length
            i += 1
        else:
            # Mismatch
            if length != 0:
                # Reduce length using previous lps value
                length = lps[length - 1]
            else:
                # No prefix found
                lps[i] = 0
                i += 1
    
    return lps

def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    results = []

    if m == 0:
        return results
    
    # Build LPS array
    lps = build_lps_array(pattern)

    i = 0  # pointer for text
    j = 0  # pointer for pattern

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        
        if j == m:
            # Pattern found
            results.append(i - j)
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            # Mismatch after j matches
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return results

# Example usage
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
matches = kmp_search(text, pattern)
print(f"Pattern '{pattern}' found at indices: {matches}")
# Output: Pattern 'ABABCABAB' found at indicies: [10]