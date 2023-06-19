import streamlit as st
import pandas as pd

# Criar um dataframe de exemplo
data = {
    'Anos': ['2019', '2020', '2021', '2022'],
    'Idade': [ 413205.44, 96832.90, 312646.21, 382404.09 ],
    'Fornecedores': ['Tam', 'Gol', 'Omega', 'Celular Funcional']
}

df = pd.DataFrame(data)

# Exibir a tabela
st.table(df)







