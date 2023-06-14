def generate_frequency_dictionary(string):
    frequency_dict = {}
    for char in string:
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1
    return frequency_dict
