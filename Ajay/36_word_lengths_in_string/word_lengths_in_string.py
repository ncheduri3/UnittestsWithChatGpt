def length_of_each_word(s):
    # Remove leading and trailing spaces
    s = s.strip()

    # Split the string by spaces
    words = s.split()

    # Calculate the length of each word
    word_lengths = [len(word) for word in words]

    return word_lengths
