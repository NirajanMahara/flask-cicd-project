from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask Gemini Project!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
