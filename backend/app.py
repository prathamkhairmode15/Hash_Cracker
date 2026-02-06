from flask import Flask, request, jsonify
from flask_cors import CORS
from core.dictionary_attack import dictionary_attack

app = Flask(__name__)
CORS(app)   # <-- THIS LINE FIXES YOUR ISSUE

@app.route("/")
def home():
    return "Backend is running"

@app.route("/api/dictionary-attack", methods=["POST"])
def run_dictionary_attack():
    data = request.get_json()

    target_hash = data.get("hash")
    algorithm = data.get("algorithm")

    if not target_hash or not algorithm:
        return jsonify({"status": "error", "message": "Invalid input"}), 400

    result = dictionary_attack(target_hash, algorithm)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
