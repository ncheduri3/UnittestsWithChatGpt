def transpose_strings(string_list):
    transposed = []
    for i in range(len(string_list[0])):
        column = ''.join(string[i] for string in string_list)
        transposed.append(column)
    return transposed
