from flask import Flask, render_template, request
from flask_socketio import SocketIO, join_room, emit

from crypto import caesar, affine, aes, railfence, row_transposition, playfair

app = Flask(__name__)
socketio = SocketIO(app)

# 🔐 Encrypt
def encrypt_message(msg, algo, key):
    if algo == "Caesar":
        return caesar.encrypt(msg, int(key))
    elif algo == "Affine":
        a, b = map(int, key.split(","))
        return affine.encrypt(msg, a, b)
    elif algo == "AES":
        return aes.encrypt(msg, key)
    elif algo == "RailFence":
        return railfence.encrypt(msg, int(key))
    elif algo == "RowTransposition":
        return row_transposition.encrypt(msg, key)
    elif algo == "Playfair":
        return playfair.encrypt(msg, key)
    return msg

# 🔓 Decrypt
def decrypt_message(cipher, algo, key):
    try:
        if algo == "Caesar":
            return caesar.decrypt(cipher, int(key))
        elif algo == "Affine":
            a, b = map(int, key.split(","))
            return affine.decrypt(cipher, a, b)
        elif algo == "AES":
            return aes.decrypt(cipher, key)
        elif algo == "RailFence":
            return railfence.decrypt(cipher, int(key))
        elif algo == "RowTransposition":
            return row_transposition.decrypt(cipher, key)
        elif algo == "Playfair":
            return playfair.decrypt(cipher, key)
    except:
        return None

# 🏠 Home (join page)
@app.route("/")
def index():
    return render_template("index.html")

# 💬 Chat page
@app.route("/chat", methods=["POST"])
def chat():
    name = request.form["name"]
    room = request.form["room"]
    algo = request.form["algo"]
    key = request.form["key"]

    return render_template("chat.html", name=name, room=room, algo=algo, key=key)

# 🔥 Join room
@socketio.on("join")
def handle_join(data):
    join_room(data["room"])
    emit("status", {"msg": data["name"] + " joined"}, room=data["room"])

# 🔥 Send message
@socketio.on("send_message")
def handle_message(data):
    room = data["room"]

    cipher = encrypt_message(data["message"], data["algo"], data["key"])

    decrypted = None
    if data["algo"] == data["receiver_algo"] and data["key"] == data["receiver_key"]:
        decrypted = decrypt_message(cipher, data["receiver_algo"], data["receiver_key"])

    emit("receive_message", {
        "name": data["name"],
        "cipher": cipher,
        "decrypted": decrypted
    }, room=room)

if __name__ == "__main__":
    socketio.run(app, debug=True)