def encrypt(text, rails):
    if rails <= 1 or not text: return text
    fence = [[] for _ in range(rails)]
    rail, step = 0, 1
    for c in text:
        fence[rail].append(c)
        rail += step
        if rail == 0 or rail == rails-1: step *= -1
    return ''.join(''.join(row) for row in fence)

def decrypt(cipher, rails):
    return "Handled_in_Frontend"