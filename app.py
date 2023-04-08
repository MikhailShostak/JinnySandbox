from flask import Flask, request
import hashlib
import base64

app = Flask(__name__)

@app.route('/hash/<algorithm>', methods=['POST'])
def hash(algorithm):
    data = request.data
    if algorithm == 'md5':
        hashed_data = hashlib.md5(data).hexdigest()
    elif algorithm == 'sha1':
        hashed_data = hashlib.sha1(data).hexdigest()
    elif algorithm == 'sha256':
        hashed_data = hashlib.sha256(data).hexdigest()
    elif algorithm == 'sha512':
        hashed_data = hashlib.sha512(data).hexdigest()
    else:
        return 'Invalid algorithm', 400
    return hashed_data

@app.route('/encode/<algorithm>', methods=['POST'])
def encode(algorithm):
    data = request.data
    if algorithm == 'base64':
        encoded_data = base64.b64encode(data).decode('utf-8')
    else:
        return 'Invalid algorithm', 400
    return encoded_data

@app.route('/decode/<algorithm>', methods=['POST'])
def decode(algorithm):
    data = request.data
    if algorithm == 'base64':
        decoded_data = base64.b64decode(data).decode('utf-8')
    else:
        return 'Invalid algorithm', 400
    return decoded_data
