import base64
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
from main import env_variables
key=env_variables['KEY']

def encrypt(raw):
    data = str(raw)
    encoded_raw = pad(data.encode(), 16)
    cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    return base64.b64encode(cipher.encrypt(encoded_raw)).decode('utf-8')

def decrypt(enc):
    enc = base64.b64decode(enc)
    cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    return unpad(cipher.decrypt(enc), 16)

# print(decrypt(encrypt("data_here")))