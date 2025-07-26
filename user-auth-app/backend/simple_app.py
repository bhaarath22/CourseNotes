from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/test', methods=['GET'])
def test():
    return jsonify({"message": "Backend is working!", "status": "success"})

@app.route('/api/signup', methods=['POST'])
def simple_signup():
    return jsonify({"message": "Signup endpoint working", "status": "success"}), 201

@app.route('/api/login', methods=['POST'])
def simple_login():
    return jsonify({"message": "Login endpoint working", "status": "success"}), 200

if __name__ == '__main__':
    print("Starting simplified Flask app...")
    app.run(host='0.0.0.0', port=5000, debug=True)