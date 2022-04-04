from asyncio.windows_events import NULL
from flask import Flask,render_template, request
 
app = Flask(__name__)

@app.route("/",methods =["POST","GET"])
def calculate():
    resultado =""
    if request.method == "POST":
        operador1 =float(request.form.get("op1"))
        operador2 =float(request.form.get("op2"))
        calculo = str(request.form.get("calc"))
        if op =="soma":
            resultado = round(n1+n2)
        elif op =="subtracao":
            resultado = round(n1-n2)
        elif op == "divisao":
            resultado =round(n1/n2)
        elif op == "multiplicacao":
            resultado = round(n1*n2)
    if resultado == 0 or resultado == NULL:
        resultado = str(0)
    return render_template("index.html",resultado = resultado)