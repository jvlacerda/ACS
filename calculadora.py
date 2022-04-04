from asyncio.windows_events import NULL
from flask import Flask,render_template, request
 
app = Flask(__name__)

@app.route("/",methods =["POST","GET"])
def calculate():
    resultado =""
    if request.method == "POST":
        op1 =float(request.form.get("op1"))
        op2 =float(request.form.get("op2"))
        calc = str(request.form.get("calc"))
        if calc =="soma":
            resultado = round(op1+op2)
        elif calc =="subtracao":
            resultado = round(op1-op2)
        elif calc == "divisao":
            resultado =round(op1/op2)
        elif calc == "multiplicacao":
            resultado = round(op1*op2)
    if resultado == 0 or resultado == NULL:
        resultado = str(0)
    return render_template("index.html",resultado = resultado)
    
if __name__ == '__main__':
   app.run(debug=True, host='localhost', port=5000)