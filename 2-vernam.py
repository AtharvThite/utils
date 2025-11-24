import string

ALPHABET = string.ascii_uppercase

def vernam_encrypt(plaintext, key):
    ciphertext = ""
    for p, k in zip(plaintext, key):
        p_val = ord(p) - ord('A')
        k_val = ord(k) - ord('A')
        c_val = p_val ^ k_val
        ciphertext += ALPHABET[c_val]
    return ciphertext

def vernam_decrypt(ciphertext, key):
    plaintext = ""
    for c, k in zip(ciphertext, key):
        c_val = ord(c) - ord('A')
        k_val = ord(k) - ord('A')
        p_val = c_val ^ k_val
        plaintext += ALPHABET[p_val]
    return plaintext


# Example
plaintext = "HELLO"
key = "XMCKL"   # <-- give any key same length

cipher = vernam_encrypt(plaintext, key)
decrypted = vernam_decrypt(cipher, key)

print("Plaintext :", plaintext)
print("Key       :", key)
print("Cipher    :", cipher)
print("Decrypted :", decrypted)
