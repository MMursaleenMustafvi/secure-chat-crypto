def encrypt(text, shift):
    result = ""
    for c in text:
        if c.isalpha():
            result += chr((ord(c.upper()) + shift - 65) % 26 + 65)
        else: result += c
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)