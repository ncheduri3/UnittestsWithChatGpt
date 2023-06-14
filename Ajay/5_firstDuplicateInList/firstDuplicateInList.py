def first_duplicate_in_list(lst):
    seen = set()
    for item in lst:
        if item in seen:
            return item
        seen.add(item)
    return None
