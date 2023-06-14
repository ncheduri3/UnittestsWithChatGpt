import re


def substring_occurs_twice(string, substring):
    pattern = r'\b' + re.escape(substring) + r'\b'
    matches = re.findall(pattern, string)
    return len(matches) == 2
