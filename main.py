from flask import Flask, render_template
from apimercadopago import gerar_link_pagamento

app = Flask(__name__)

@app.route("/")
def homepage():
    link_iniciar_pagamento = gerar_link_pagamento()
    return render_template("homepage.html", link=link_iniciar_pagamento)

@app.route("/compracerta")
def compracerta():
    return "<h1>✅ Pagamento aprovado com sucesso!</h1>"

@app.route("/compraerrada")
def compraerrada():
    return "<h1>❌ Pagamento não foi concluído.</h1>"

if __name__ == "__main__":
    app.run(port=5000)
