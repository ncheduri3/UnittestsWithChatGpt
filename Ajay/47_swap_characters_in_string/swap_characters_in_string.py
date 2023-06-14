def swap_characters(string, i, j):
    if i < 0 or i >= len(string) or j < 0 or j >= len(string):
        # Invalid indices, return the original string
        return string
    
    # Convert the string to a list to make swapping easier
    characters = list(string)
    
    # Swap the characters at indices i and j
    characters[i], characters[j] = characters[j], characters[i]
    
    # Convert the list back to a string and return it
    return ''.join(characters)
