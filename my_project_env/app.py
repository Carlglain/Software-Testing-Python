# app.py
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    test= "L5oo next year"
    return jsonify(message="Hello level 400 FET, Quality Assurance! " + test)


if __name__ == '__main__':
    app.run(debug=True)