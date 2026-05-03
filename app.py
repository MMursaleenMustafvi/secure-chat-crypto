from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, join_room, emit
from crypto import caesar, affine, aes, railfence, row_transposition, playfair

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-pro-key'
socketio = SocketIO(app)

def encrypt_message(msg, algo, key):
    try:
        if algo == "Caesar": 
            return caesar.encrypt(msg, int(key)) if key.strip().lstrip('-').isdigit() else "INVALID_KEY_NOT_A_NUMBER"
        elif algo == "Affine": 
            try:
                a, b = map(int, key.split(","))
                return affine.encrypt(msg, a, b)
            except:
                return "INVALID_AFFINE_FORMAT_USE_COMMA"
        elif algo == "AES": 
            return aes.encrypt(msg, key)
        elif algo == "RailFence": 
            return railfence.encrypt(msg, int(key)) if key.strip().isdigit() else "INVALID_KEY_NOT_A_NUMBER"
        elif algo == "RowTransposition": 
            return row_transposition.encrypt(msg, key)
        elif algo == "Playfair": 
            return playfair.encrypt(msg, key)
    except Exception as e:
        print(f"Encryption Error: {e}")
        return "CRITICAL_ENCRYPTION_ERROR"
    return msg

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST", "GET"])
def chat():
    if request.method == "GET": return redirect(url_for("index"))
    name = request.form.get("name", "Anonymous")
    room = request.form.get("room", "General")
    algo = request.form.get("algo", "AES")
    key = request.form.get("key", "")
    return render_template("chat.html", name=name, room=room, algo=algo, key=key)

@socketio.on("join")
def handle_join(data):
    join_room(data["room"])
    emit("status", {"msg": f"{data['name']} has entered the secure zone."}, room=data["room"])

@socketio.on("send_message")
def handle_message(data):
    room = data["room"]
    cipher = encrypt_message(data["message"], data["algo"], data["key"])
    
    emit("receive_message", {
        "name": data["name"],
        "original_msg": data["message"],
        "cipher": cipher,
        "sender_algo": data["algo"],
        "sender_key": data["key"]
    }, room=room)

if __name__ == "__main__":
    socketio.run(app, debug=True)