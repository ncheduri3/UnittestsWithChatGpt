def caesar_cipher(string, key):
    result = ""
    for char in string:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - ascii_offset + key) % 26 + ascii_offset)
            result += shifted_char
        else:
            result += char
    return result
