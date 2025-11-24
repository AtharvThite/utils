def mono_encrypt(text, key):
    cipher = ""
    text = text.upper()
    for ch in text:
        if ch.isalpha():
            cipher += key[ord(ch) - 65]
        else :
            cipher += ch
    return cipher

def mono_decrypt(cipher, text):
    rev = {key[i]: chr(65+i) for i in range(26)}
    text = ""
    for ch in cipher.upper():
        if ch.isalpha():
            text += rev[ch]
        else:
            text += ch
    return text

key = "QWERTYUIOPASDFGHJKLZXCVBNM"
enc = mono_encrypt("HELLO", key)
dec = mono_decrypt(enc, key)
print(enc, dec)