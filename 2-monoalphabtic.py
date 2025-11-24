def mono_encrypt(text, key):
    text = text.lower()
    cipher = ""
    for ch in text:
        if ch.isalpha():
            cipher += key[ord(ch) - 97]
        else:
            cipher += ch
    return cipher

def mono_decrypt(cipher, text):
    cipher = cipher.lower()
    text = ""
    mapping = {key[i]: chr(i+97) for i in range(26)}
    for ch in cipher:
        if ch.isalpha():
            text += mapping[ch]
        else:
            text += ch
    return text

key = "QWERTYUIOPASDFGHJKLZXCVBNM"
enc = mono_encrypt("HELLO", key)
dec = mono_decrypt(enc, key)
print(enc, dec)