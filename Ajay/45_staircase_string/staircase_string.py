def staircase_string(string):
    length = len(string)
    out = []
    for i in range(1, length + 1):
        out.append(string[:i])
    return out
