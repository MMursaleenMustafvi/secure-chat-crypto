from Crypto.Cipher import AES
import base64

def pad(text):
    while len(text) % 16 != 0: text += ' '
    return text

def encrypt(msg, key):
    try:
        if not key: key = "defaultkey"
        key = key.ljust(16)[:16].encode()
        cipher = AES.new(key, AES.MODE_ECB)
        enc = cipher.encrypt(pad(msg).encode())
        return base64.b64encode(enc).decode()
    except Exception: return "AES_ENCRYPT_ERROR"

def decrypt(cipher_text, key):
    return "Handled_in_Frontend"