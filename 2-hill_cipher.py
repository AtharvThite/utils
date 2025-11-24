import numpy as np

def hill_encrypt(text, key):
    text = text.replace(" ", "").lower()
    if len(text) % 2 != 0:
        text += 'x'

    cipher = ""
    for i in range(0, len(text), 2):
        mat = np.array([[ord(text[i]) - 97],
                        [ord(text[i+1]) - 97]])
        enc = np.dot(key, mat) % 26
        cipher += chr(enc[0][0] + 97) + chr(enc[1][0] + 97)
    return cipher


def mod_matrix_inverse(matrix, mod):
    det = int(round(np.linalg.det(matrix)))
    det = det % mod

    for i in range(mod):
        if (det * i) % mod == 1:
            det_inv = i
            break
    else:
        print("Matrix is not invertible.")
        return

    adj = np.array([[matrix[1][1], -matrix[0][1]],
                    [-matrix[1][0], matrix[0][0]]])

    inv_matrix = (det_inv * adj) % mod
    return inv_matrix


def hill_decrypt(cipher, key):
    key_inv = mod_matrix_inverse(key, 26)

    text = ""
    for i in range(0, len(cipher), 2):
        mat = np.array([[ord(cipher[i]) - 97],
                        [ord(cipher[i+1]) - 97]])
        dec = np.dot(key_inv, mat) % 26
        text += chr(dec[0][0] + 97) + chr(dec[1][0] + 97)
    return text

key = np.array([[3, 3],
                [2, 5]])

enc = hill_encrypt("help", key)
dec = hill_decrypt(enc, key)

print("Encrypted:", enc)
print("Decrypted:", dec)
