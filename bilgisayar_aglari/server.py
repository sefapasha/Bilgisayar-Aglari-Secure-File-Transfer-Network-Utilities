import socket
from encryption import aes_decrypt, rsa_decrypt, generate_keys, hash_sha256
from fragmenter import reassemble

host = '0.0.0.0'
port = 5050
s = socket.socket()
s.bind((host, port))
s.listen(1)

conn, addr = s.accept()

# RSA anahtar üret
priv, pub = generate_keys()
conn.send(pub)

aes_key = rsa_decrypt(conn.recv(256), priv)

data = b''
while True:
    chunk = conn.recv(1024)
    if not chunk:
        break
    data += chunk

print(f"Gelen veri boyutu: {len(data)} byte")
dec_data = aes_decrypt(data, aes_key)
file_data, received_hash = dec_data.split(b'||')


if hash_sha256(file_data).encode() == received_hash:
    with open('received_file.txt', 'wb') as f:
        f.write(file_data)
    print("Dosya bütünlüğü doğrulandi ve kaydedildi.")
else:
    print("Bütünlük hatasi!")

conn.close()
