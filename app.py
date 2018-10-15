from flask import Flask


app = Flask(__name__)


@app.route("/")
def ola():
    return "<h1> Olá Servidor python </h1>"


if __name__ == "__main__":
    app.run()