import requests
import streamlit as st

def obter_gastos_por_parlamentar(nome_deputado):
    url_base = "https://dadosabertos.camara.leg.br/api/v2/"
    endpoint = f"deputados?nome={nome_deputado}"
    url = url_base + endpoint

    try:
        response = requests.get(url)
        if response.status_code == 200:
            dados = response.json()
            deputado_id = dados['dados'][0]['id']
            endpoint_gastos = f"deputados/{deputado_id}/despesas?ano=2019,2020,2021,2022"
            url_gastos = url_base + endpoint_gastos
            response_gastos = requests.get(url_gastos)
            if response_gastos.status_code == 200:
                dados_gastos = response_gastos.json()
                gastos_totais = sum(despesa['valorLiquido'] for despesa in dados_gastos['dados'])
                return gastos_totais
            else:
                return None
        else:
            return None
    except requests.exceptions.RequestException as e:
        return None

# Interface do Streamlit
st.title("Consulta de Gastos por Parlamentar")

# Entrada do nome do deputado
nome_deputado = st.text_input("Digite o nome do deputado")

# Botão para consultar os gastos
if st.button("Consultar Gastos"):
    if nome_deputado:
        gastos_parlamentar = obter_gastos_por_parlamentar(nome_deputado)
        if gastos_parlamentar is not None:
            st.write(f"Total de gastos do deputado {nome_deputado} entre 2019 e 2022: R$ {gastos_parlamentar:.2f}")
        else:
            st.write("Não foi possível obter os gastos do parlamentar.")
    else:
        st.write("Por favor, digite o nome do deputado.")
        import csv

def calcular_fornecedoras_mais_recebem(dados):
    fornecedoras = {}
    
    for dado in dados:
        ano = dado['Ano']
        fornecedora = dado['Fornecedora']
        valor = float(dado['Valor'])
        
        if ano >= 2019 and ano <= 2022:
            if fornecedora in fornecedoras:
                fornecedoras[fornecedora] += valor
            else:
                fornecedoras[fornecedora] = valor
    
    fornecedoras_ordenadas = sorted(fornecedoras.items(), key=lambda x: x[1], reverse=True)
    
    return fornecedoras_ordenadas

# Carregar dados do arquivo CSV
dados = []
with open('dados.csv', 'r', newline='') as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        dados.append(linha)

# Calcular as fornecedoras que mais receberam quotas financeiras
fornecedoras_mais_recebem = calcular_fornecedoras_mais_recebem(dados)

# Imprimir o resultado
for fornecedora, valor in fornecedoras_mais_recebem:
    print(f"{fornecedora}: R${valor:.2f}")












