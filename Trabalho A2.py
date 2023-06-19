import streamlit as st
import pandas as pd

# Criar um dataframe de exemplo
data = {
    'Nome': ['João', 'Maria', 'Pedro', 'Ana'],
    'Idade': [25, 30, 28, 35],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Curitiba', 'Porto Alegre']
}

df = pd.DataFrame(data)

# Exibir a tabela
st.table(df)
import streamlit as st
import numpy as np

# Criar uma matriz NumPy de exemplo
data = np.random.randn(5, 3)

# Exibir a tabela
st.table(data)








