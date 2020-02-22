from flask import Flask
import hashlib
import os

# Config Values
USERNAME = 'admin'
PASSWORD = 'password123'
UPLOAD_FOLDER = './app/static/uploads'

# SECRET_KEY is needed for session security, the flash() method in this case stores the message in a session
key = hashlib.sha3_512(os.urandom(24))
key = key.hexdigest()
SECRET_KEY = key
app = Flask(__name__)
app.config.from_object(__name__)
from app import views