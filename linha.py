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


# Função em que retornará os valores de energia (kwh) gerados em  n dias ao longo de um ano
def valores_kwh(dados):
    return [kwh for data, kwh in ordenar(dados)]


# Função em que será chamada em "def ApresentarGraficoDeLinha()", ou seja, passará os
# dados das coordenadas de entrada para o gráfico
def FiltrarEntrada():
    x = []
    y = []
    for dia in range(len(valores_kwh(informacoes))):
        y.append(valores_kwh(informacoes)[dia])
        x.append(dia + 1)
        # Retorno da função com os dados preenchidos com os eixos x e y
    return x, y


# Função de geração de gráfico usando a biblioteca matplotlib
def GerarGrafico(x, y):
    plt.style.use("ggplot")
    plt.figure(figsize=(11, 6))
    plt.plot(x, y, color='green')
    plt.title('ENERGIA GERADA AO LONGO DE UM ANO', color='w')
    plt.xlabel('DIAS DO ANO', color='w')
    plt.ylabel('ENERGIA GERADA POR DIA (kwh)', color='w')
    plt.grid(True, alpha=.4)
    plt.xticks(color='w')
    plt.yticks(color='w')
    plt.legend(['kwh'], bbox_to_anchor=(1.12, 0.5), loc=5, borderaxespad=0.)
    plt.savefig('linha.png', facecolor='k', transparent=True)
    plt.close()


# Função que será chamada no arquivo main
def ApresentarGraficoDeLinha():
    tuplaDados = FiltrarEntrada()
    GerarGrafico(tuplaDados[0], tuplaDados[1])
