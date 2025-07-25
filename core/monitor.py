import time
from bot.cotacao_crypto_service import pegar_cotacao
from bot.telegram_service import enviar_mensagem
from config.settings import INTERVALO_APOS_ALERTA, INTERVALO_CHECAGEM, MONITORAMENTOS

ultimo_alerta = {moeda: 0 for moeda in MONITORAMENTOS}

def inciar_monitoramento():
  while True:
        for moeda_id, conf in MONITORAMENTOS.items():
            try:
                preco = pegar_cotacao(moeda_id)
                nome = conf["nome"]
                print(f"[INFO] Preço atual da {nome}: R${preco:.2f}")

                agora = time.time()
                tempo_desde_alerta = agora - ultimo_alerta[moeda_id]

                if preco >= conf["limite_superior"] and tempo_desde_alerta >= INTERVALO_APOS_ALERTA:
                    mensagem = f"🚨 A {nome} subiu para R${preco:.2f}!\nHora de vender!"
                    enviar_mensagem(mensagem)
                    ultimo_alerta[moeda_id] = agora

                elif preco <= conf["limite_inferior"] and tempo_desde_alerta >= INTERVALO_APOS_ALERTA:
                    mensagem = f"🚨 A {nome} caiu para R${preco:.2f}!\nPode ser hora de comprar!"
                    enviar_mensagem(mensagem)
                    ultimo_alerta[moeda_id] = agora

            except Exception as erro:
                print(f"[ERRO] Monitorando {moeda_id}: {erro}")
        
        time.sleep(INTERVALO_CHECAGEM)