import json
#função para calcular a media
def calcMedia(dados):
  dias = 0;
  acumulador = 0.0
  media = 0.0
  for dado in dados:
    if(dado['valor'] != 0.0):
      dias++;
      acumulador +=dado['valor']
  #calculo da media
  media = acumulador / dias
  return media

with open("dados.json", encoding='utf-8') as meu_json:
    dados = json.load(meu_json)

for dado in dados:
  print('No dia',dado['dia'],'o valor foi de',dado['valor'])
