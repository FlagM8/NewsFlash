# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route("/home")
def home_page():
    return 'hello world hihi kith'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port="5001",debug=True)