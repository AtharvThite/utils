def gcd(a, b):
    if a < b : a,b = b,a
    r1 = a
    r2 = b
    while r2 != 0:
        q = r1 // r2
        r = r1 % r2
        r1, r2 = r2, r
    return r1

# Function to find modular inverse
def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d

# RSA Key Generation
def rsa_keygen(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 2
    while e < phi:
        if gcd(e, phi) == 1:
            break
        e += 1

    # Find d (private key exponent)
    d = mod_inverse(e, phi)

    return (e, n), (d, n)     # public key, private key

# Encryption
def rsa_encrypt(msg, public_key):
    e, n = public_key
    return (msg ** e) % n

# Decryption
def rsa_decrypt(cipher, private_key):
    d, n = private_key
    return (cipher ** d) % n

p = 11
q = 13

public_key, private_key = rsa_keygen(p, q)

msg = 9
cipher = rsa_encrypt(msg, public_key)
plain  = rsa_decrypt(cipher, private_key)

print("Public Key :", public_key)
print("Private Key:", private_key)
print("Original Message:", msg)
print("Encrypted:", cipher)
print("Decrypted:", plain)
