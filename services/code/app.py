from flask import Flask
from pymongo import MongoClient
from .env import SECRET_KEY
import os

MONGO_URI = os.environ.get('MONGO_URI')

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
client = MongoClient(MONGO_URI)
db = client["nfdb"]
