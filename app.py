from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Hello from CI/CD!",
        "status": "running"
    })
    
@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

@app.route("/profile")
def profile():
    return "Welcome User"

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if data.get("username") == "admin" and data.get("password") == "secret":
        return jsonify({"message": "Login successful"}), 200

    return jsonify({"message": "Invalid credentials"}), 401

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)