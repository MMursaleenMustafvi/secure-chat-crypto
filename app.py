from flask import Flask, render_template, request
from crypto import caesar, affine, aes

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    cipher = ""
    result = ""

    if request.method == "POST":
        message = request.form["message"]
        algo = request.form["algorithm"]
        key = request.form["key"]

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
            result = "Error: Invalid key or input"

    return render_template("index.html", cipher=cipher, result=result)


if __name__ == "__main__":
    app.run(debug=True)