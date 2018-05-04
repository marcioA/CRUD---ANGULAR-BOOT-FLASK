from app import app
from flask import render_template, url_for


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cadastrar")
def cadastrar():
    return render_template("cadastro.html")

@app.route("/cadastro", methods=['GET', 'POST'])
def cadastroExec():
    if request.method == "POST":
        nome = request.form.get("nome")
        cpf = request.form.get("cpf")
        email = request.form.get("email")
        senhaUser = request.form.get("senhaUser")
        senhaUserConf = request.form.get("senhaUserConf")
