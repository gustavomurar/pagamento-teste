import mercadopago

def gerar_link_pagamento():
    sdk = mercadopago.SDK("APP_USR-1808471496143612-101921-809d20ec45e3cf2d5d94f8ed1a9ddbf4-2932784903")

    # 🔹 Substitua aqui pelo seu domínio público gerado pelo ngrok
    NGROK_URL = "https://xxxx.ngrok.io"

    payment_data = {
        "items": [
            {
                "id": "1",
                "title": "Camisa",
                "quantity": 1,
                "currency_id": "BRL",
                "unit_price": 259.99
            }
        ],
        "back_urls": {
            "success": f"{NGROK_URL}/compracerta",
            "failure": f"{NGROK_URL}/compraerrada",
            "pending": f"{NGROK_URL}/compraerrada",
        },
        "auto_return": "all"
    }

    result = sdk.preference().create(payment_data)

    print("\n==============================")
    print("🔍 Resultado da API Mercado Pago:")
    print(result)
    print("==============================\n")

    payment = result.get("response", {})

    if "init_point" not in payment:
        print("⚠️ Erro: resposta inesperada do Mercado Pago.")
        return "ERRO: resposta inválida. Veja o terminal para detalhes."

    return payment["init_point"]
