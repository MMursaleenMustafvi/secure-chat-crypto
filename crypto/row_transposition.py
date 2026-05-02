def encrypt(message, key):
    col = len(key)
    row = len(message) // col + (len(message) % col != 0)

    matrix = [['' for _ in range(col)] for _ in range(row)]

    idx = 0
    for i in range(row):
        for j in range(col):
            if idx < len(message):
                matrix[i][j] = message[idx]
                idx += 1

    order = sorted(list(enumerate(key)), key=lambda x: x[1])

    cipher = ""
    for i, _ in order:
        for r in matrix:
            cipher += r[i]

    return cipher


def decrypt(cipher, key):
    col = len(key)
    row = len(cipher) // col

    order = sorted(list(enumerate(key)), key=lambda x: x[1])

    matrix = [['' for _ in range(col)] for _ in range(row)]

    idx = 0
    for i, _ in order:
        for j in range(row):
            matrix[j][i] = cipher[idx]
            idx += 1

    result = ""
    for r in matrix:
        result += ''.join(r)

    return result.strip()