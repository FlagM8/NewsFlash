from flask import Flask
from pymongo import MongoClient
from config import MONGO_URI, SECRET_KEY

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
client = MongoClient(MONGO_URI)
db = client["your_database_name"]
