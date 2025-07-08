from flask import Flask, render_template, request, jsonify
from crypto.aes_util import encrypt_message, decrypt_message

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/encrypt", methods=["POST"])
def encrypt():
    data = request.get_json()
    text = data.get("text")
    key = data.get("key")
    encrypted = encrypt_message(text, key)
    return jsonify({"result": encrypted})

@app.route("/decrypt", methods=["POST"])
def decrypt():
    data = request.get_json()
    text = data.get("text")
    key = data.get("key")
    decrypted = decrypt_message(text, key)
    return jsonify({"result": decrypted})

if __name__ == "__main__":
    app.run(debug=True)
