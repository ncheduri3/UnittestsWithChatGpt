def find_substrings_with_char(string, char):
    substrings = set()
    length = len(string)
    for i in range(length):
        if string[i] == char:
            for j in range(i, length):
                substrings.add(string[i:j+1])
    return sorted(list(substrings))
