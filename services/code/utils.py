from flask import Flask, request, jsonify, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS
import jwt
import datetime




"""def findByName(username):
    return app.db.users.find_one({"username" : username})

def findByEmail(email):
    return app.db.users.find_one({"email" : email})"""

def findUser(email = None, username = None):
        """Returns a user based on email or username."""
        if email is not None:
            return current_app.db.users.find_one({"email" : email})
        elif username is not None:
            return current_app.db.users.find_one({"username" : username})

    