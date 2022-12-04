"""
this module include the setup to encrypt and decrypt data using pycryptodome
and crypto-js for client side.
Credit:
1: https://medium.com/@sachadehe/encrypt-decrypt-data-between-python-3-and-javascript-true-aes-algorithm-7c4e2fa3a9ff
2: https://pycryptodome.readthedocs.io/en/latest/#
3: https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.1.1/crypto-js.min.js
"""

import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def encrypt(raw, key):
    """taking raw data and converting into string then making cipher using AES"""
    data = str(raw)
    encoded_raw = pad(data.encode(), 16)
    # AES(Advanced Encryption Standard)
    cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    return base64.b64encode(cipher.encrypt(encoded_raw)).decode('utf-8')

def decrypt(enc, key):
    """
    taking encrypted data and firstly decoding data form back from b64 then
    using AES instance method decrypting the encrypted data.
    """
    enc = base64.b64decode(enc)
    cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    return unpad(cipher.decrypt(enc), 16)

def decrypt_in_js():
    """
    <html lang="en">
        <body>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.1.1/crypto-js.min.js"></script>
            <script>
            var encrypted =
                "SWBoEbQmmNXQCntYDW0foClQC1kO2khFzyLygn63nh2jsPNJw0+Cc6RcdTFMpZgiXR4LPfPj7lpGflT5BopnWf2qn6rywWmuF1i7GHskcI4="
            var key = "AAAAAAAAAAAAAAAA"; //key used in Python
            key = CryptoJS.enc.Utf8.parse(key);
            var decrypted = CryptoJS.AES.decrypt(encrypted, key, {
                mode: CryptoJS.mode.ECB,
            });
            console.log(decrypted.toString(CryptoJS.enc.Utf8));
            </script>
        </body>
    </html>
    """
    pass