def generate_word(s: str) -> str:
    words = s.split()
    generated_word = ''
    for i, word in enumerate(words):
        if len(word) > i:
            generated_word += word[i]
    return generated_word
