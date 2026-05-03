def mod_inverse(a, m):
    for i in range(m):
        if (a * i) % m == 1: return i
    return 1 

def encrypt(text, a, b):
    try:
        result = ""
        for c in text:
            if c.isalpha():
                x = ord(c.upper()) - 65
                result += chr((a*x + b) % 26 + 65)
            else: result += c
        return result
    except: return "AFFINE_ERROR"

def decrypt(text, a, b):
    return "Handled_in_Frontend"