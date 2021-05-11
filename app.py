from flask import Flask, jsonify, request, g, render_template
from flask_cors import CORS
from werkzeug import exceptions
import sqlite3

app = Flask(__name__)
CORS(app)

DATABASE = "./database/database.db"

@app.route('/')
def home():
  return jsonify({'message': 'Welcome!'}), 200

if __name__ == "__main__":
    app.run(debug=True)