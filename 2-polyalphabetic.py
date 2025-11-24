def poly_encrypt(text, key):
    result = ""
    key = key.lower()
    j = 0
    for ch in text:
        if ch.isalpha():
            base = ord('a')
            shift = ord(key[j % len(key)]) - base
            result += chr((ord(ch.lower()) - base + shift) % 26 + base)
            j += 1
        else:
            result += ch
    return result

def poly_decrypt(text, key):
    result = ""
    key = key.lower()
    j = 0
    for ch in text:
        if ch.isalpha():
            base = ord('a')
            shift = ord(key[j % len(key)]) - base
            result += chr((ord(ch.lower()) - base - shift) % 26 + base)
            j += 1
        else:
            result += ch
    return result

print(poly_encrypt("hello", "key"))
print(poly_decrypt("rijvs", "key"))
