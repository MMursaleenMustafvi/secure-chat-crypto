def mod_inverse(a, m):
    for i in range(m):
        if (a * i) % m == 1:
            return i
    return None

def encrypt(text, a, b):
    result = ""
    for char in text:
        if char.isalpha():
            x = ord(char) - 65
            result += chr((a * x + b) % 26 + 65)
    return result

def decrypt(text, a, b):
    a_inv = mod_inverse(a, 26)
    result = ""
    for char in text:
        x = ord(char) - 65
        result += chr((a_inv * (x - b)) % 26 + 65)
    return result