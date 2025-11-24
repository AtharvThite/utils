import socket

def gcd(a, b):
    if a < b : a,b = b,a
    r1 = a
    r2 = b
    while r2 != 0:
        q = r1 // r2
        r = r1 % r2
        r1, r2 = r2, r
    return r1

def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d

def rsa_keygen(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 2
    while e < phi:
        if gcd(e, phi) == 1:
            break
        e += 1
    d = mod_inverse(e, phi)
    return (e, n), (d, n)     # public key, private key

def rsa_decrypt(cipher, private_key):
    d, n = private_key
    return (cipher ** d) % n

# Generate RSA keys
public_key, private_key = rsa_keygen(11, 13)
e, n = public_key

print("Server Public Key:", public_key)
print("Server Private Key:", private_key)

s = socket.socket()
s.bind(("localhost", 3000))
s.listen(1)

print("Server running on port 3000")
conn, addr = s.accept()
print("Client connected:", addr)

# Send public key to client
conn.send(f"{e},{n}".encode())

# Receive ciphertext
cipher = int(conn.recv(1024).decode())
print("\nReceived Ciphertext:", cipher)

# Decrypt message
msg = rsa_decrypt(cipher, private_key)
print("Decrypted Message:", msg)

conn.close()
s.close()
