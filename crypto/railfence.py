def encrypt(text, rails):
    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1

    for char in text:
        fence[rail].append(char)
        rail += direction

        if rail == 0 or rail == rails - 1:
            direction *= -1

    return ''.join([''.join(row) for row in fence])


def decrypt(cipher, rails):
    pattern = [[] for _ in range(rails)]
    rail = 0
    direction = 1

    for _ in cipher:
        pattern[rail].append('*')
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction *= -1

    index = 0
    for i in range(rails):
        for j in range(len(pattern[i])):
            pattern[i][j] = cipher[index]
            index += 1

    result = ""
    rail = 0
    direction = 1

    for _ in cipher:
        result += pattern[rail].pop(0)
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction *= -1

    return result