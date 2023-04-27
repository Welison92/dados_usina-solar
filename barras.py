# Bibliotecas do Sistema
import matplotlib.pyplot as plt
import json
import urllib.request as req

# Endereço do qual se obterá uma resposta no formato JSON. Representa os dados
# gerados (potencia, ecomoniaDia, datas e entre outros) em uma usina solar durante um ano (2019).
url = "http://albertocn.sytes.net/2019-2/pi/projeto/geracao_energia.json"

# Cria uma requisição para a URL passada e define no cabeçalho um browser conhecido como
# cliente (agent) para que o site não proíba o acesso
requisicao = req.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

try:
    # Isto faz com que a URL seja acessa e todo o seu conteúdo seja lido
    # e guardado na variável "dados"
    dados = req.urlopen(requisicao).read().decode()
    dados_proc = json.loads(dados)
except:
    print('deu erro :(')

informacoes = []
# Loop utilizado para pegar os dias e o  total de kwh gerado em n dia da variável
# "dados_proc", com isso, são guardados todos os dados na variável "informacoes"
for dados in dados_proc:
    if "dia" in dados:
        informacoes.append((dados["dia"], dados["energiaDia"]))


# Função criada com o objetivo em ordenar os dados contidos em uma variável
def ordenar(dados):
    return [ordenando for ordenando in sorted(dados)]


# Função em que pega as datas e os kwh gerados em n dias de um determinado mês, nesse caso,
# o respectivo mês utilizado na coleta de dados foi o mês de Janeiro
def mes(dados):
    mes = []
    for dia in range(len(ordenar(dados)) - 334):
        mes.append(ordenar(dados)[dia])
    return mes


# Função em que tem como objetivo pegar os kwh gerados em n dias do mês
def valores_kwh(dados):
    kwhs = []
    for data, kwh in mes(dados):
        kwhs.append(kwh)
    return kwhs


# Função em que será chamada em "def ApresentarGraficoDeBarras()", ou seja, passará os
# dados das coordenadas de entrada para o gráfico
def FiltrarEntrada():
    y = []
    x = []
    for dia in range(len(valores_kwh(informacoes))):
        y.append(valores_kwh(informacoes)[dia])
        x.append(dia + 1)
    # Retorno da função com os dados preenchidos com os eixos x e y
    return (x, y)


# Função de geração de gráfico usando a biblioteca matplotlib
def GerarGrafico(x, y):
    plt.style.use("ggplot")
    plt.figure(figsize=(11, 6))
    plt.bar(x, y, color='green')
    plt.title('ENERGIA GERADA POR DIA NO MÊS DE JANEIRO', color='w')
    plt.xlabel('DIAS DO MÊS', color='w')
    plt.ylabel('ENERGIA GERADA (Kwh)', color='w')
    plt.grid(True, alpha=.4)
    plt.xticks(color='w')
    plt.yticks(color='w')
    plt.legend(['kwh'], bbox_to_anchor=(1.12, 0.5), loc=5, borderaxespad=0.)
    plt.savefig('barras.png', facecolor='k', transparent=True)
    plt.close()


# Função que será chamada no arquivo main
def ApresentarGraficoDeBarras():
    tuplaDados = FiltrarEntrada()
    GerarGrafico(tuplaDados[0], tuplaDados[1])
