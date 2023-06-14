def generate_string(n, k):
    result = ""
    for i in range(n):
        result += chr(k + i)
    return result
