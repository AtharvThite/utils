def ceasar_encrypt(text, key):
    cipher = ""
    for c in text:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            cipher += chr((ord(c)-base+key)%26 + base)
        else:
            cipher += c
    return cipher

def ceasar_decrypt(cipher, key):
    text = ceasar_encrypt(cipher, -key)
    return text

print(ceasar_encrypt("HELLO", 3))
print(ceasar_decrypt("KHOOR", 3))