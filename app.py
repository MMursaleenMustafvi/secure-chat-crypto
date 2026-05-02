from flask import Flask, render_template
from flask_socketio import SocketIO, emit

from crypto import caesar, affine, aes

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat")
def chat():
    return render_template("chat.html")

# 🔥 REAL-TIME MESSAGE HANDLER
@socketio.on("send_message")
def handle_message(data):
    message = data["message"]
    algo = data["algorithm"]
    key = data["key"]

    cipher = ""
    result = ""

    try:
        if algo == "Caesar":
            shift = int(key)
            cipher = caesar.encrypt(message, shift)
            result = caesar.decrypt(cipher, shift)

        elif algo == "Affine":
            a, b = map(int, key.split(","))
            cipher = affine.encrypt(message, a, b)
            result = affine.decrypt(cipher, a, b)

        elif algo == "AES":
            cipher = aes.encrypt(message, key)
            result = aes.decrypt(cipher, key)

    except:
        result = "❌ Error"

    emit("receive_message", {
        "cipher": cipher,
        "result": result,
        "algorithm": algo
    }, broadcast=True)

if __name__ == "__main__":
    socketio.run(app, debug=True)