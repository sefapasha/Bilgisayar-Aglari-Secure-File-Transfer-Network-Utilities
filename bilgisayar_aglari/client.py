import socket
import os
from encryption import aes_encrypt, rsa_encrypt, hash_sha256
from fragmenter import fragment

server_ip = '127.0.0.1'
server_port = 5050

s = socket.socket()
s.connect((server_ip, server_port))

# AES anahtarı oluşturalım
aes_key = os.urandom(16)
public_key = s.recv(1024)
s.send(rsa_encrypt(aes_key, public_key))

# Dosyayı okuma
filename = 'file_to_send.txt'
with open(filename, 'rb') as f:
    data = f.read()

# Sha256 hash ile bütünlük
hash_val = hash_sha256(data).encode()

# Şifrele ve fragmente et
enc_data = aes_encrypt(data + b'||' + hash_val, aes_key)
fragments = fragment(enc_data)


s.send(enc_data)

s.close()
