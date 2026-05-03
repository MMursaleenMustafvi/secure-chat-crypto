def encrypt(text, shift):
    try:
        result = ""
        for c in text:
            if c.isalpha():
                result += chr((ord(c.upper()) + shift - 65) % 26 + 65)
            else: result += c
        return result
    except: return "CAESAR_ERROR"

def decrypt(text, shift):
    return "Handled_in_Frontend"