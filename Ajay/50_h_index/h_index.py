def h_index(citations):
    citations.sort(reverse=True)  # Sort the citations in descending order
    h = 0

    for i, citation in enumerate(citations):
        if citation >= i + 1:
            h = i + 1
        else:
            break

    return h
