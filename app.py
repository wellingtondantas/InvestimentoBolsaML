
#Importação de Pacotes
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as web
import streamlit as st

import time


#title
st.markdown("<h1 style='color:#F00;'>Modelo de Predição de Preço de Ações da Bolsa de Valores</h1>", unsafe_allow_html=True)
#sub-title
st.subheader("""
App que utiliza inteligência articial para prever subida ou descida de ação. \n\n
""")

#Obtem os indices da bovesta
idxBov = pd.read_csv('resource/indices.csv', sep=';', encoding="ISO-8859-1")


#Seleciona o indice para analise
option = st.selectbox('Escolha o índice papel que deseja analisar', idxBov)
x = option.split(" - ", 1)

'Você selecionou: ', x[0]

st.markdown("<font color='#00F'>Defina a sua Pesquisa</font>", unsafe_allow_html=True)
'''
Selecione o ano, mês e dia
'''

#Seleciona o ano
st.sidebar.markdown('Início')
year = st.sidebar.slider("Ano de Apuração", 2012, 2019, 2015)
month = st.sidebar.slider("Mês de Apuração", 1, 12, 6)
day = st.sidebar.slider("Dia de Apuração", 1, 31, 15)


#Obtem os dados históricos
df = web.DataReader(str(x[0])+'.SA', data_source='yahoo', start=str(year)+'-'+str(month)+'-'+str(day), end='2021-01-02') 

st.markdown("<font color='#00F'>Histórico de Preços da Ação</font>", unsafe_allow_html=True) 
st.dataframe(df)


progress_bar = st.progress(0)
status_text = st.empty()
last_rows = np.random.randn(1, 1)
chart = st.line_chart(last_rows)

for i in range(1, 101):
    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    status_text.text("%i%% Complete" % i)
    chart.add_rows(new_rows)
    progress_bar.progress(i)
    last_rows = new_rows
    time.sleep(0.1)

progress_bar.empty()

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")



