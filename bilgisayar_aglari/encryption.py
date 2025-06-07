from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
import hashlib

# RSA anahtar çifti üretir (2048 bit)
def generate_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

# Veriyi RSA ile şifreler (alıcıya public key gönderilir)
def rsa_encrypt(data, pub_key):
    key = RSA.import_key(pub_key)
    cipher_rsa = PKCS1_OAEP.new(key)
    return cipher_rsa.encrypt(data)

# RSA ile şifrelenmiş veriyi çözer (private key ile)
def rsa_decrypt(enc_data, priv_key):
    key = RSA.import_key(priv_key)
    cipher_rsa = PKCS1_OAEP.new(key)
    return cipher_rsa.decrypt(enc_data)

# AES ile veriyi şifreler (EAX modu kullanır)
def aes_encrypt(data, key):
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    # nonce (16 byte) + tag (16 byte) + ciphertext
    return cipher.nonce + tag + ciphertext

# AES ile şifreli veriyi çözer (nonce ve tag çıkarılır)
def aes_decrypt(encrypted_data, key):
    nonce = encrypted_data[:16]
    tag = encrypted_data[16:32]
    ciphertext = encrypted_data[32:]
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    return cipher.decrypt_and_verify(ciphertext, tag)

# SHA-256 hash hesaplar (veri bütünlüğü için)
def hash_sha256(data):
    return hashlib.sha256(data).hexdigest()
