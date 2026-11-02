from flask import Flask, jsonify

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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)