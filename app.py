from flask import Flask


server = Flask(__name__)


@server.route("/")
def ola():
    return "<h1> Olá Servidor python </h1>"


if __name__ == "__main__":
    server.run()