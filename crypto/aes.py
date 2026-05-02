from Crypto.Cipher import AES
import base64

def pad(text):
    while len(text) % 16 != 0:
        text += ' '
    return text

def encrypt(message, key):
    key = key.ljust(16)[:16].encode()
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted = cipher.encrypt(pad(message).encode())
    return base64.b64encode(encrypted).decode()

def decrypt(cipher_text, key):
    key = key.ljust(16)[:16].encode()
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = cipher.decrypt(base64.b64decode(cipher_text))
    return decrypted.decode().strip()