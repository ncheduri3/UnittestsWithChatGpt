def indices_of_occurrences(string, char):
    indices = []
    for i in range(len(string)):
        if string[i] == char:
            indices.append(i)
    return indices
