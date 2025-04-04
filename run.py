"""Starting point"""
from flask import Flask, request, jsonify
from app.users import Users
from app.devices import Devices


app = Flask(__name__)


@app.route("/")
def hello():
    return 'Hello, World'

@app.route("/login", methods=['POST'])
def login():

    try:
        users = Users()
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")
        role = users.validate_user(username, password)
        if role:
            return jsonify({"role": role}), 200
        else:
            return jsonify({"error": "Invalid credentials"}), 401
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/devices", methods=['GET'])
def get_devices():
    try:
        devices = Devices()
        data = devices.get_devices()
        if data:
            return jsonify({"data": data}), 200
        else:
            return jsonify({"error": "Not Found"}), 401
    except Exception as e:
        return jsonify({"error": str(e)}), 500
