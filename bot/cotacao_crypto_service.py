import requests

def pegar_cotacao(moeda: str) -> float:
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={moeda}&vs_currencies=brl"
    response = requests.get(url)
    data = response.json()
    return data[moeda]["brl"]
