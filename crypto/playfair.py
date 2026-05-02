def generate_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    used = set()

    for char in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in used:
            matrix.append(char)
            used.add(char)

    return [matrix[i:i+5] for i in range(0, 25, 5)]


def find_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j


def prepare_text(text):
    text = text.upper().replace("J", "I")
    result = ""

    i = 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else 'X'

        if a == b:
            result += a + 'X'
            i += 1
        else:
            result += a + b
            i += 2

    if len(result) % 2 != 0:
        result += 'X'

    return result


def encrypt(text, key):
    matrix = generate_matrix(key)
    text = prepare_text(text)
    result = ""

    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        if r1 == r2:
            result += matrix[r1][(c1+1)%5] + matrix[r2][(c2+1)%5]
        elif c1 == c2:
            result += matrix[(r1+1)%5][c1] + matrix[(r2+1)%5][c2]
        else:
            result += matrix[r1][c2] + matrix[r2][c1]

    return result


def decrypt(text, key):
    matrix = generate_matrix(key)
    result = ""

    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        if r1 == r2:
            result += matrix[r1][(c1-1)%5] + matrix[r2][(c2-1)%5]
        elif c1 == c2:
            result += matrix[(r1-1)%5][c1] + matrix[(r2-1)%5][c2]
        else:
            result += matrix[r1][c2] + matrix[r2][c1]

    return result