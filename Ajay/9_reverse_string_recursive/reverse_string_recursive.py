def reverse_string_recursive(string):
    if len(string) <= 1:
        return string
    return reverse_string_recursive(string[1:]) + string[0]
