import requests
import streamlit as st
import matplotlib.pyplot as plt

def obter_gastos_por_parlamentar(nome_deputado):
    url_base = "https://dadosabertos.camara.leg.br/api/v2/deputados"
    endpoint = f"?nome={nome_deputado}"
    url = url_base + endpoint

    try:
        response = requests.get(url)
        if response.status_code == 200:
            dados = response.json()
            deputado_id = dados['dados'][0]['id']
            endpoint_gastos = f"/{deputado_id}/despesas?ano=2019,2020,2021,2022"
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

total = 0
fornecedores = {}
cnpjCpfFornecedores = {}
for pag in range(1, 100):
  u = f'https://dadosabertos.camara.leg.br/api/v2/deputados/178939/despesas?ano=2019&ano=2020&ano=2021&ano=2022&ordem=ASC&ordenarPor=ano&pagina={pag}&itens=100'
  r = requests.get(u).json()
  for gasto in r['dados']:
    valor = float(gasto['valorLiquido'])
    total = total + valor
    nome = gasto['nomeFornecedor']
    cnpjCpf = gasto['cnpjCpfFornecedor']
    if cnpjCpf not in cnpjCpfFornecedores:
      cnpjCpfFornecedores[cnpjCpf] = valor
      fornecedores[cnpjCpf] = nome
    else:
      cnpjCpfFornecedores[cnpjCpf] = cnpjCpfFornecedores[cnpjCpf] + valor

print (f'Total retornado API Câmara: R$ {total:.2f}')
def chave(f): return f[1]
maiores = sorted(cnpjCpfFornecedores.items(), key=chave, reverse=True)

st.write("Gráfico de gastos fornecedores")

def criar_grafico():
    # Dados para o gráfico de exemplo
    x = [maiores[1][1], maiores[2][1], maiores[3][1], maiores[4][1], maiores[5][1]]
    y = [2019,2020,2021,2022]

    # Criar o gráfico de linhas
    plt.plot(x, y)

    # Exibir o gráfico
    st.pyplot(plt)

chart_data = pd.top5(
    np.random.randn(20, 3),
    columns=["2019", "2020", "2021",2022])

st.bar_chart(chart_data)
