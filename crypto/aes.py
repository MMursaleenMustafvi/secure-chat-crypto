from Crypto.Cipher import AES
import base64

def pad(text):
    while len(text) % 16 != 0:
        text += ' '
    return text

def encrypt(msg, key):
    key = key.ljust(16)[:16].encode()
    cipher = AES.new(key, AES.MODE_ECB)
    enc = cipher.encrypt(pad(msg).encode())
    return base64.b64encode(enc).decode()

def decrypt(cipher_text, key):
    key = key.ljust(16)[:16].encode()
    cipher = AES.new(key, AES.MODE_ECB)
    dec = cipher.decrypt(base64.b64decode(cipher_text))
    return dec.decode().strip()