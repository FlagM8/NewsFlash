from flask import Blueprint, request, jsonify
from flask_bcrypt import Bcrypt
from app import db
from flask_jwt_extended import create_access_token

bcrypt = Bcrypt()
auth = Blueprint("auth", __name__)

@auth.route('/register', methods=['POST'])
def register():
    data = request.json
    hashed_password = bcrypt.generate_password_hash(data["password"]).decode('utf-8')
    user = {
        "username": data['username'],
        "email": data['email'],
        "password": hashed_password,
        "preferences": []
    }
    db.users.insert_one(user)
    return jsonify({"message": "User registered successfully"}), 201

@auth.route('/login', methods=['POST'])
def login():
    data = request.json
    user = db.users.find_one({"username": data['username']})
    if user and bcrypt.check_password_hash(user['password'], data['password']):
        token = create_access_token(identity=user['username'])
        return jsonify({"token": token}), 200
    return jsonify({"message": "Invalid credentials"}), 401