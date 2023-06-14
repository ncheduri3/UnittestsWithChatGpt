def longest_repeating_substring(s):
    n = len(s)
    longest_substring = ""
    
    for i in range(n):
        for j in range(i+1, n):
            substring = ""
            k = 0
            
            # Check for repetitions
            while j+k < n and s[i+k] == s[j+k]:
                substring += s[i+k]
                k += 1
            
            # Update the longest repeating substring
            if k > 1 and len(substring) > len(longest_substring):
                longest_substring = substring
    
    return longest_substring
