from flask import Flask, jsonify
from datetime import datetime
import random

app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify({"message": "Hello from Flask!"})

@app.route("/time")
def time():
    return jsonify({"time": datetime.now().isoformat()})

@app.route("/random")
def rand():
    return jsonify({"random": random.randint(1, 100)})

if __name__ == "__main__":
    app.run(debug=True)
