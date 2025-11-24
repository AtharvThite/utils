import socket

def rsa_encrypt(msg, public_key):
    e, n = public_key
    return pow(msg, e, n)

s = socket.socket()
s.connect(("localhost", 5000))

# Receive public key
data = s.recv(1024).decode()
e, n = map(int, data.split(","))
public_key = (e, n)

print("Received Public Key:", public_key)

# Message to send
msg = 9
cipher = rsa_encrypt(msg, public_key)

print("Original Message:", msg)
print("Encrypted:", cipher)

# Send ciphertext to server
s.send(str(cipher).encode())

s.close()