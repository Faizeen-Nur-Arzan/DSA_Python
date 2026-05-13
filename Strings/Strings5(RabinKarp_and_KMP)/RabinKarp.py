def rabin_karp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    matches = []

    # Choose a prime number for hashing
    # Larger prime = fewer hask collisions
    prime = 101
    base = 256  # We can use 256 for all ASCII characters
    mod = 10**9 + 7  # Large prime to prevent overflow

    # Step 1: Calculate the highest power needed
    # For pattern "ABC" with m = 3: base ^ (m - 1) = 256 ^ 2
    # We'lluse this to remove the first character
    h = 1
    for i in range(m - 1):
        h = (h * base) % mod
    
    # Step 2: Compute hash of pattern and first window of text
    pattern_hash = 0
    window_hash = 0

    # Calculate hash for pattern
    for i in range(m):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % mod
    
    #Calculate hash for first window of text
    for i in range(m):
        window_hash = (base * window_hash + ord(pattern[i])) % mod
    
    # Step 3: slide the window through the text
    for i in range(n - m + 1):
        # Check if hashes match
        if pattern_hash == window_hash:
            # Hash collision possible! Verify actual strings
            if text[i:i+m] == pattern:
                matches.append(i)
                print(f"Match found at index {i}")
        
        # Step 4 & 5: Calculate hash for next window using rolling hash
        if i < n - m:
            # Remove first character of current window and add new character
            # Formula: new_hash = (old_hash - first_char * h) * base + new_char
            window_hash = (base * (window_hash - ord(text[i]) * h) + ord(text[i + m])) % mod

            # Handle negative values (modulo of negative number)
            if window_hash < 0:
                window_hash += mod
    
    return matches

# Example 1: Simple pattern
text1 = "ABABDABACDABABCABAB"
pattern1 = "ABAB"
print(f"Searching for '{pattern1}' in '{text1}'")
result1 = rabin_karp_search(text1, pattern1)
print(f"Matches at positions: {result1}\n")

# Example 2: Multiple occurences
text2 = "AABAABAAAB"
pattern2 = "AAB"
print(f"Searching for '{pattern2}' in '{text2}'")
result2 = rabin_karp_search(text2, pattern2)
print(f"Matches at positions: {result2}\n")