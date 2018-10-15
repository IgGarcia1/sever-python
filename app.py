from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route("/", methods=["GET"])
def ola():
    return "<h1> Olá Servidor python </h1>"

@app.route("/", methods=["POST"])

def main():
    from corretor.Controller import Controller
    from corretor.ConversorJson import ConversorJson
    from deleteFiles import deleteFiles

    dados = request.get_json() # pegando dados
    
    user = dados['user']
    codigo = dados['code']
    entradas = dados['enters']

    try:
        c = Controller(entradas, codigo, user)  
    except:
        deleteFiles( str(user)+'.txt',str(user)+'.json')
        return "Error"
    else:
        nameJson = ConversorJson(user, append=True).returnFileJson()

        arquivoPronto =  open(nameJson).read()

        deleteFiles( str(user)+'.txt',nameJson) # deletando arquivos para nao sobrecarregar

        return jsonify(saidas = arquivoPronto)

if __name__ == "__main__":
    app.run()