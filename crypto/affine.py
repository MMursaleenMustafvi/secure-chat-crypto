def mod_inverse(a, m):
    for i in range(m):
        if (a * i) % m == 1: return i
    return 1 # Fallback to prevent crashes

def encrypt(text, a, b):
    result = ""
    for c in text:
        if c.isalpha():
            x = ord(c.upper()) - 65
            result += chr((a*x + b) % 26 + 65)
        else: result += c
    return result

def decrypt(text, a, b):
    a_inv = mod_inverse(a, 26)
    result = ""
    for c in text:
        if c.isalpha():
            x = ord(c.upper()) - 65
            result += chr((a_inv*(x-b)) % 26 + 65)
        else: result += c
    return result