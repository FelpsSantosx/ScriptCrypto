from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("TOKENBOT")
CHAT_ID = os.getenv("IDCHAT")

MONITORAMENTOS = {
    "ripple": {
        "nome": "XRP",
        "limite_superior": 21.22,
        "limite_inferior": 12.96,
    },
    "cardano": {
        "nome": "ADA",
        "limite_superior": 5.50,
        "limite_inferior": 3.50,
    },
    "stellar": {
        "nome": "XLM",
        "limite_superior": 3.21,
        "limite_inferior": 1.68,
    },
    "matic-network": {
        "nome": "MATIC",
        "limite_superior": 4.82,
        "limite_inferior": 0.50,
    }
}

INTERVALO_CHECAGEM = 60  # em segundos
INTERVALO_APOS_ALERTA = 60 * 60 * 5  # 5 horas