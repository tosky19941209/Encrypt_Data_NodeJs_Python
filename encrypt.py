# from flask import Flask, request, jsonify
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64
import json

app = Flask(__name__)

SECRET_KEY = b'mysecretkey1234'  # This should be 16, 24, or 32 bytes long for AES
BLOCK_SIZE = 16  # AES block size is 16 bytes

# Encrypt data using AES
def encrypt_data(data):
    cipher = AES.new(SECRET_KEY, AES.MODE_CBC)  # CBC mode
    json_data = json.dumps(data)
    padded_data = pad(json_data.encode(), BLOCK_SIZE)  # Pad data to be multiple of BLOCK_SIZE
    iv = cipher.iv  # Initialization vector (IV) is generated automatically
    encrypted_data = cipher.encrypt(padded_data)  # Encrypt data
    encrypted_data_with_iv = base64.b64encode(iv + encrypted_data).decode('utf-8')  # Combine IV and encrypted data
    return encrypted_data_with_iv

# Decrypt data using AES
def decrypt_data(encrypted_data_with_iv):
    encrypted_data_with_iv = base64.b64decode(encrypted_data_with_iv.encode('utf-8'))
    iv = encrypted_data_with_iv[:BLOCK_SIZE]  # Extract IV
    encrypted_data = encrypted_data_with_iv[BLOCK_SIZE:]  # Extract encrypted data
    
    cipher = AES.new(SECRET_KEY, AES.MODE_CBC, iv)  # Use the same IV for decryption
    decrypted_data = unpad(cipher.decrypt(encrypted_data), BLOCK_SIZE)  # Decrypt and remove padding
    return json.loads(decrypted_data.decode('utf-8'))  # Convert bytes back to original data



response_data = {
    'message': 'Hello, this is a secret message!',
    'timestamp': '2024-11-27T12:34:56',
}
encrypted_response = encrypt_data(response_data)

decrypted_response = decrypt_data(encrypted_response)

print(encrypted_response)
print(decrypted_response)