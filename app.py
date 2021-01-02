
#Importação de Pacotes
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as web
import streamlit as st




#title
st.markdown("<h1 style='color:#F00;'>Modelo de Predição de Preço de Ações da Bolsa de Valores</h1>", unsafe_allow_html=True)
#sub-title
st.subheader("""
App que utiliza inteligência articial para prever subida ou descida de ação. \n\n
""")


#Obtem os indices da bovesta
idxBov = pd.read_csv('resource/indices.csv', sep=';', encoding="ISO-8859-1")

#Seleciona o indice para analise
option = st.selectbox('Escolha o índice papel que deseja analisar', idxBov['Papel'])

'Você selecionou: ', option

#Obtem os dados históricos
df = web.DataReader('VALE3.SA', data_source='yahoo', start='2012-01-01', end='2020-04-17') 

st.write("Histórico de Preços da Ação")
st.write(df)


