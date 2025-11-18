from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/soma")
def index():
    return render_template("index.html")


@app.route("/soma")
def somar():
    numero1 = request.args.get("cebolinha",type=int)
    numero2 = request.args.get("nomeQualquer",type=int)
    total= numero1 + numero2
    return {"operecao":"soma","resultado":total}

@app.route("/subtrair")
def subtrair():
    numero1 = request.args.get("valor1", type=int)
    numero2 = request.args.get("valor2",type=int)
    total = numero1 - numero2
    return {"operacao":"subtracao","resultado":f"{numero1}-{numero2} = {total}"}

@app.route("/mutiplicar")
def mutiplicar():
    numero1 = request.args.get("valor1", type=int)
    numero2 = request.args.get("valor2",type=int)
    total = numero1 * numero2
    return {"operacao":"mutplicacao","resultado":f"{numero1}X{numero2} = {total}"}

@app.route("/dividir")
def dividir():
    numero1 = request.args.get("valor1",type=int)
    numero2 = request.args.get("valor2",type=int)
    if numero2 == 0:
       total = numero1 / numero2
    
    return {"operacao":"divisao","resultado":f"{numero1}%{numero2} = {total}"}

if __name__ == "__main__":
    app.run(debug=True)

  