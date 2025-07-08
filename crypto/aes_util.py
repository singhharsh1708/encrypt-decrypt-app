from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib

def get_key(key: str) -> bytes:
    return hashlib.sha256(key.encode()).digest()

def encrypt_message(msg: str, key: str) -> str:
    key_bytes = get_key(key)
    cipher = AES.new(key_bytes, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(msg.encode(), AES.block_size))
    return b64encode(cipher.iv + ct_bytes).decode()

def decrypt_message(enc: str, key: str) -> str:
    try:
        enc_bytes = b64decode(enc)
        key_bytes = get_key(key)
        iv = enc_bytes[:16]
        ct = enc_bytes[16:]
        cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(ct), AES.block_size)
        return pt.decode()
    except Exception as e:
        return "Invalid decryption or key!"
