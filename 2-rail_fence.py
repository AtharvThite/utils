import numpy as np

def rail_encrypt(text, key):
    rail = [''] * key
    row = 0
    step = 1

    for ch in text:
        rail[row] += ch
        if row == 0:
            step = 1
        elif row == key - 1:
            step = -1
        row += step

    return ''.join(rail)

def rail_decrypt(cipher, key):
    # length of ciphertext
    n = len(cipher)

    # create empty matrix
    rail = np.empty((key, n), dtype=str)
    rail[:] = ''   # fill with empty strings

    # mark zig-zag positions
    row, step = 0, 1
    for i in range(n):
        rail[row][i] = '*'
        if row == 0:
            step = 1
        elif row == key - 1:
            step = -1
        row += step

    # fill matrix row-wise with ciphertext
    idx = 0
    for r in range(key):
        for c in range(n):
            if rail[r][c] == '*':
                rail[r][c] = cipher[idx]
                idx += 1

    # read plaintext in zig-zag
    result = ""
    row, step = 0, 1
    for i in range(n):
        result += rail[row][i]
        if row == 0:
            step = 1
        elif row == key - 1:
            step = -1
        row += step

    return result

cipher = rail_encrypt("HELLO WORLD", 3)
plain  = rail_decrypt(cipher, 3)

print("Encrypted:", cipher)
print("Decrypted:", plain)
