# Monitor de Preços de Criptomoedas

Monitor de preços de criptomoedas utilizando Python, requests e o Telegram.

## Tecnologias utilizadas

- [Python](https://www.python.org/)
- [Requests](https://requests.readthedocs.io/en/master/)
- [Telegram](https://core.telegram.org/)

## Como utilizar

### 1. Crie um bot do Telegram

- Abra o Telegram e procure pelo @BotFather
- Envie o comando `/start` e siga as instruções
- Anote o token do seu bot

### 2. Instale as dependências

- Clone o repositório e execute `pip install -r requirements.txt`

### 3. Configure o seu bot

- Crie um arquivo `.env` com as seguintes variáveis:
  - `TOKEN`: o token do seu bot
  - `CHAT_ID`: o ID do chat onde o bot irá enviar as mensagens
- Edite o arquivo `config/settings.py` e altere as variáveis `MONITORAMENTOS` e `INTERVALO_CHECAGEM` de acordo com as suas necessidades

### 4. Execute o script

- Execute o comando `python main.py`

## Funcionamento

- O script irá checar os preços das criptomoedas listadas em `MONITORAMENTOS` a cada `INTERVALO_CHECAGEM` segundos
- Se o preço de uma criptomoeda ultrapassar o limite superior ou inferior, o bot irá enviar uma mensagem para o chat informando o preço atual e o tempo desde a última mensagem
- O bot irá esperar `INTERVALO_APOS_ALERTA` segundos antes de enviar outra mensagem

