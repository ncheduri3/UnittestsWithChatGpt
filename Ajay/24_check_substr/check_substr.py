def is_substring(substring, string):
    if len(substring) > len(string):
        return False

    for i in range(len(string) - len(substring) + 1):
        j = 0
        while j < len(substring):
            if string[i+j] != substring[j]:
                break
            j += 1
        if j == len(substring):
            return True

    return False
