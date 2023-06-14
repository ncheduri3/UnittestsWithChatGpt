def merge_strings_by_ascii(str1, str2):
    merged = []
    i = 0
    j = 0
    while i < len(str1) and j < len(str2):
        if ord(str1[i]) <= ord(str2[j]):
            merged.append(str1[i])
            i += 1
        else:
            merged.append(str2[j])
            j += 1
    while i < len(str1):
        merged.append(str1[i])
        i += 1
    while j < len(str2):
        merged.append(str2[j])
        j += 1
    return ''.join(merged)
