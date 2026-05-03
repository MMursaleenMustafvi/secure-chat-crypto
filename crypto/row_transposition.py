def encrypt(msg, key):
    try:
        if not key or not msg: return msg
        key = str(key)
        col = len(key)
        row = (len(msg) + col - 1) // col
        matrix = [['']*col for _ in range(row)]
        k = 0
        for i in range(row):
            for j in range(col):
                if k < len(msg):
                    matrix[i][j] = msg[k]
                    k += 1
                else: matrix[i][j] = 'X'
        order = sorted(range(len(key)), key=lambda x: key[x])
        return ''.join(matrix[r][c] for c in order for r in range(row))
    except: return "ROWTRANS_ERROR"

def decrypt(cipher, key):
    return "Handled_in_Frontend"