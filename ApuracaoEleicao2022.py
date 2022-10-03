import json
import pandas as pd
import requests
import datetime
from time import sleep

x = 0

while x >= 0:
    sleep(60)
    data = requests.get(
        'https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json')

    json_data = json.loads(data.content)

    candidato = []
    partido = []
    votos = []
    porcentagem = []

    for informacoes in json_data['cand']:
        if informacoes['seq'] in ['1', '2', '3', '4']:
            candidato.append(informacoes['nm'])
            votos.append(informacoes['vap'])
            porcentagem.append(informacoes['pvap'])

    df_eleicao = pd.DataFrame(list(zip(candidato, votos, porcentagem)), columns=[
        'Candidato', 'Nº de Votos', 'Porcentagem'])

    data_hora = datetime.datetime.now()
    print(df_eleicao)

    print(f"Foi atualizado as: {data_hora} ")
    print(x)
    x = x + 1
