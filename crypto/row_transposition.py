def encrypt(msg, key):
    col = len(key)
    row = (len(msg) + col - 1) // col
    matrix = [['']*col for _ in range(row)]

    k = 0
    for i in range(row):
        for j in range(col):
            if k < len(msg):
                matrix[i][j] = msg[k]
                k += 1

    order = sorted(range(len(key)), key=lambda x: key[x])

    return ''.join(matrix[r][c] for c in order for r in range(row))

 
def decrypt(cipher, key):
    col = len(key)
    row = len(cipher) // col
    matrix = [['']*col for _ in range(row)]

    order = sorted(range(len(key)), key=lambda x: key[x])

    k = 0
    for c in order:
        for r in range(row):
            matrix[r][c] = cipher[k]
            k += 1

    return ''.join(''.join(r) for r in matrix)