# API Exemplo

### Cotação do dólar de forma automática e atualizada

### Usamos o awesome api: https://docs.awesomeapi.com.br/
        

import requests
import json

cotacoes = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
cotacoes = cotacoes.json() #vem em json e passamos para linguagem python
cotacao_dolar = cotacoes['USDBRL']['bid']
cotacao_real = cotacoes['EURBRL']['bid']
cotacao_bitcoin = cotacoes['BTCBRL']['bid']

print(cotacoes) #retorna um dicionário com vários dicionários dentro
print('A cotação do Dolar nesse momento é de:', cotacao_dolar)
print('A cotação do Real nesse momento é de:', cotacao_real)
print('A cotação do Bitcoin nesse momento é de:', cotacao_bitcoin)
