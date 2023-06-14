def countdown_strings(n):
    result = []
    for i in range(n):
        countdown = ' '.join(str(j) for j in range(i + 1, 0, -1))
        result.append(countdown)
    return result
