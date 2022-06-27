import json

#função para calcular a media
def calcMedia(dados):
  dias = 0;
  acumulador = 0.0
  media = 0.0
  for dado in dados:
    if dado['valor'] != 0.0:
      print(dado['valor'])
      dias += 1;
      acumulador +=dado['valor']
  #calculo da media
  print(acumulador,dias)
  media = acumulador / dias
  return media

#função para encontrar o menor valor no mês
def calcMenor(dados):
  #retorna o primeiro valor que não é 0.0(Zero)
  menor = dados[0]
  pos = 0
  while(menor['valor'] == 0.0):
    menor = dados[pos]
    pos += 1
  #verifica o menor de fato ignorando os valores
  for dado in dados[(pos + 1):]:
    if dado['valor'] != 0.0:
      if(menor['valor'] > dado['valor']):
        menor = dado

  return menor


if(__name__ == '__main__'):
  with open("dados.json", encoding='utf-8') as meu_json:
      dados = json.load(meu_json)
  media = calcMedia(dados)
  menor = calcMenor(dados)
  print(menor)
