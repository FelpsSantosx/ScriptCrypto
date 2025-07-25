import requests
from config.settings import TOKEN, CHAT_ID

def enviar_mensagem(mensagem: str):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": mensagem}
    response = requests.post(url, data=payload)

    if response.status_code == 200:
        print("✅ Mensagem enviada com sucesso!")
    else:
        print(f"❌ Erro ao enviar mensagem: {response.text}")
