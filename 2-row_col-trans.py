import numpy as np

def row_col_encrypt(text, key):
    text = text.replace(" ", "")
    k = [int(x) - 1 for x in key]   # convert key digits to column indexes
    
    cols = len(key)
    rows = (len(text) + cols - 1) // cols  

    # pad text
    while len(text) < rows * cols:
        text += 'x'

    # fill matrix row by row
    matrix = []
    index = 0
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(text[index])
            index += 1
        matrix.append(row)

    # read column by column using key order
    cipher = ""
    for col_index in k:
        for r in range(rows):
            cipher += matrix[r][col_index]

    return cipher

def row_col_decrypt(cipher, key):
    cipher = cipher.replace(" ", "")
    k = [int(x) - 1 for x in key]   # key digits → column indexes

    cols = len(key)
    rows = len(cipher) // cols

    # Prepare empty matrix
    matrix = np.empty((rows, cols), dtype=str)

    # Fill columns according to key order
    index = 0
    for col_index in k:    # fill column in key order
        for r in range(rows):
            matrix[r][col_index] = cipher[index]
            index += 1

    # Read matrix row by row
    plaintext = ""
    for r in range(rows):
        for c in range(cols):
            plaintext += matrix[r][c]

    return plaintext

text = "HELLOWORLD"
key = "3142"
enc = row_col_encrypt(text, key)
dec = row_col_decrypt(enc, key)
print(f"Enrypted : {enc}")
print(f"Derypted : {dec}")