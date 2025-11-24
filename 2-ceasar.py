def ceasar_encrypt(text, key):
    text = text.lower()
    cipher = ""
    for c in text:
        if c.isalpha():
            cipher += chr((ord(c)+key-97)%26 + 97)
        else:
            cipher += c
    return cipher

def ceasar_decrypt(cipher, key):
    text = ceasar_encrypt(cipher, -key)
    return text

print(ceasar_encrypt("HELLO", 3))
print(ceasar_decrypt("KHOOR", 3))