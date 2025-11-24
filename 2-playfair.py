def generate_matrix(key):
    key = key.replace("j", "i")
    matrix = []
    for ch in key:
        if ch not in matrix and ch.isalpha():
            matrix.append(ch)
    for ch in "abcdefghiklmnopqrstuvwxyz":
        if ch not in matrix:
            matrix.append(ch)
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_pos(matrix, ch):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                return i, j

def playfair_encrypt(text, key):
    matrix = generate_matrix(key.lower())
    text = text.replace("j", "i")
    text = text.replace(" ", "")

    # Make digraphs
    pairs = []
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else 'x'
        if a == b:
            b = 'x'
            i += 1
        else:
            i += 2
        pairs.append((a, b))

    result = ""
    for a, b in pairs:
        r1, c1 = find_pos(matrix, a)
        r2, c2 = find_pos(matrix, b)

        if r1 == r2:  # same row
            result += matrix[r1][(c1+1)%5] + matrix[r2][(c2+1)%5]
        elif c1 == c2:  # same column
            result += matrix[(r1+1)%5][c1] + matrix[(r2+1)%5][c2]
        else:  # rectangle swap
            result += matrix[r1][c2] + matrix[r2][c1]

    return result

def playfair_decrypt(cipher, key):
    matrix = generate_matrix(key.lower())
    cipher = cipher.replace("j", "i")
    cipher = cipher.replace(" ", "")

    # Split ciphertext into digraphs
    pairs = [(cipher[i], cipher[i+1]) for i in range(0, len(cipher), 2)]

    result = ""
    for a, b in pairs:
        r1, c1 = find_pos(matrix, a)
        r2, c2 = find_pos(matrix, b)

        if r1 == r2:  # same row → shift left
            result += matrix[r1][(c1-1)%5] + matrix[r2][(c2-1)%5]

        elif c1 == c2:  # same column → shift up
            result += matrix[(r1-1)%5][c1] + matrix[(r2-1)%5][c2]

        else:  # rectangle swap (same as encryption)
            result += matrix[r1][c2] + matrix[r2][c1]

    return result

text = "hello"
key = "keyword"
enc = playfair_encrypt(text, key)
dec = playfair_decrypt(enc, key)
print(f"Enrypted : {enc}")
print(f"Derypted : {dec}")
