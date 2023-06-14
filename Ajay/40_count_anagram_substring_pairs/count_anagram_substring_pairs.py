def count_anagram_substring_pairs(string):
    # Create a dictionary to store the frequency of substrings
    substr_freq = {}
    count = 0

    # Iterate through all possible substrings
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            # Extract the substring and sort its characters
            substring = ''.join(sorted(string[i:j]))

            # Increment the count of the corresponding frequency in the dictionary
            substr_freq[substring] = substr_freq.get(substring, 0) + 1

    # Count the number of pairs of anagram substrings
    for freq in substr_freq.values():
        # If there are k occurrences of a substring, there are k*(k-1)/2 pairs
        count += freq * (freq - 1) // 2

    return count
