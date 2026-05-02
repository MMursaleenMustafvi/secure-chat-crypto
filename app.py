from flask import Flask, render_template, request
from crypto import caesar, affine, aes, railfence, row_transposition, playfair

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    cipher = ""
    result = ""
    error = ""

    if request.method == "POST":
        message = request.form.get("message", "")
        algo = request.form.get("algorithm", "")
        key = request.form.get("key", "")

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

            elif algo == "RailFence":
                rails = int(key)
                cipher = railfence.encrypt(message, rails)
                result = railfence.decrypt(cipher, rails)

            elif algo == "RowTransposition":
                cipher = row_transposition.encrypt(message, key)
                result = row_transposition.decrypt(cipher, key)

            elif algo == "Playfair":
                cipher = playfair.encrypt(message, key)
                result = playfair.decrypt(cipher, key)

            else:
                error = "❌ Invalid Algorithm Selected"

        except Exception as e:
            error = f"❌ Error: {str(e)}"

    return render_template(
        "index.html",
        cipher=cipher,
        result=result,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)