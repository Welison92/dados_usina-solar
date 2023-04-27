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


primavera = []
# Loop utilizado para pegar os valores kwh diários gerados no período da estação
# primavera, com isso, guardará os dados na variável "primavera"
for dia in range(len(valores_kwh(informacoes))):
    if 265 <= dia <= 355:
        primavera.append(valores_kwh(informacoes)[dia])

verao = []
# Loop utilizado para pegar os valores kwh diários gerados no período da estação
# verão, com isso, guardará os dados na variável "verao"
for dia in range(len(valores_kwh(informacoes))):
    if 356 <= dia <= 365 or 0 <= dia <= 77:
        verao.append(valores_kwh(informacoes)[dia])

outono = []
# Loop utilizado para pegar os valores kwh diários gerados no período da estação
# outono, com isso, guardará os dados na variável "outono"
for dia in range(len(valores_kwh(informacoes))):
    if 78 <= dia <= 171:
        outono.append(valores_kwh(informacoes)[dia])

inverno = []
# Loop utilizado para pegar os valores kwh diários gerados no período da estação
# inverno, com isso, guardará os dados na variável "inverno"
for dia in range(len(valores_kwh(informacoes))):
    if 172 <= dia <= 264:
        inverno.append(valores_kwh(informacoes)[dia])


# Função em que será chamada em "def ApresentarGraficoBoxplot()", ou seja, passará os
# dados das coordenadas de entrada para o gráfico
def FiltrarEntrada():
    valor1 = [kwh for kwh in primavera]
    valor2 = [kwh for kwh in verao]
    valor3 = [kwh for kwh in outono]
    valor4 = [kwh for kwh in inverno]

    y = [valor1, valor2, valor3, valor4]
    x = ["PRIMAVERA", "VERÃO", "OUTONO", "INVERNO"]

    # Retorno da função com os dados preenchidos com os eixos x e y
    return x, y


# Função de geração de gráfico usando a biblioteca matplotlib
def GerarGrafico(x, y):
    plt.figure(figsize=(11, 6))
    plt.boxplot(y, labels=x)
    plt.title('ENERGIA GERADA AO LONGO DE CADA ESTAÇÃO')
    plt.xlabel('ESTAÇÕES DO ANO')
    plt.ylabel('ENERGIA GERADA (Kwh)')
    plt.grid(False)
    plt.savefig('boxplot.png')
    plt.close()


# Função que será chamada no arquivo main
def ApresentarGraficoBoxplot():
    tuplaDados = FiltrarEntrada()
    GerarGrafico(tuplaDados[0], tuplaDados[1])
