def encrypt(text, rails):
    fence = [[] for _ in range(rails)]
    rail, step = 0, 1

    for c in text:
        fence[rail].append(c)
        rail += step
        if rail == 0 or rail == rails-1:
            step *= -1

    return ''.join(''.join(row) for row in fence)


def decrypt(cipher, rails):
    pattern = [[] for _ in range(rails)]
    rail, step = 0, 1

    for _ in cipher:
        pattern[rail].append('*')
        rail += step
        if rail == 0 or rail == rails-1:
            step *= -1

    idx = 0
    for r in pattern:
        for i in range(len(r)):
            r[i] = cipher[idx]
            idx += 1

    result = ""
    rail, step = 0, 1

    for _ in cipher:
        result += pattern[rail].pop(0)
        rail += step
        if rail == 0 or rail == rails-1:
            step *= -1

    return result