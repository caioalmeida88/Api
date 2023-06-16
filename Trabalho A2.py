import streamlit as st
import pandas as pd
import numpy as np
total = 0
for pag in range(1, 10):
  u = f'https://dadosabertos.camara.leg.br/api/v2/deputados/178939/despesas?ano=2022&ano=2023&ordem=ASC&ordenarPor=ano&pagina={pag}&itens=100'
  r = requests.get(u).json()
  for gasto in r['dados']:
    total = total + float(gasto['valorLiquido'])

print (f'Gasto em 2022 e 2023: R$ {total:.2f}')
