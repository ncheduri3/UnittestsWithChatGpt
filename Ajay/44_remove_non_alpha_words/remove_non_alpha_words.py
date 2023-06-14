import re


def remove_non_alpha_words(string):
    words = string.split()
    rem_lst = [word if re.match(r'^[a-zA-Z]+$', word) else '' for word in words]
    cleaned_lst = []
    for i in rem_lst:
        if i != '':
            cleaned_lst.append(i)
    return ' '.join(cleaned_lst)
