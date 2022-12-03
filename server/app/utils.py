"""this module include the setup to encrypt and decrypt data"""

import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

from main import env_variables
key=env_variables['KEY']

def encrypt(raw):
    """taking raw data and converting into string then making cipher using AES"""
    data = str(raw)
    encoded_raw = pad(data.encode(), 16)
    cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    return base64.b64encode(cipher.encrypt(encoded_raw)).decode('utf-8')

def decrypt(enc):
    """taking encrypted data and decrypting it using AES"""
    enc = base64.b64decode(enc)
    cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    return unpad(cipher.decrypt(enc), 16)

print(decrypt(encrypt("data_here")))
