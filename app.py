# app.py
from flask import Flask, jsonify

app = Flask(__name__) ;


@app.route('/Path_Test') #this is a random path just for continues testing
def home():
    return jsonify(message="Hello level 400 FET, Quality Assurance!")


if __name__ == '__main__':
    app.run(debug=True)
