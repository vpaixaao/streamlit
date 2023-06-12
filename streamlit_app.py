import streamlit as st

## Botão    
st.title("Criando um botão")

result = st.button("click here")

st.write(result)

if result:
     st.write(":smile:")
     
# aula  do dia 8
import streamlit as st
from datetime import time, datetime

st.header('st.slider')

# Exemplo 1

st.subheader('Slider')

age = st.slider('Quantos anos você tem?', 0, 130, 25)
st.write("Eu tenho ", age, ' anos')

# Exemplo 2

st.subheader('Slider de intervalo')

values = st.slider(
     'Escolha um intervalo de valores',
     0.0, 100.0, (25.0, 75.0))
st.write('Valores:', values)

# Exemplo 3

st.subheader('Slider de intervalo de tempo')

appointment = st.slider(
     "Agende um compromisso:",
     value=(time(11, 30), time(12, 45)))
st.write("O compromisso foi agendado para:", appointment)

# Exemplo 4

st.subheader('Slider de data e hora')

start_time = st.slider(
     "Quando você vai começar?",
     value=datetime(2020, 1, 1, 9, 30),
     ## só formatar o tipo de data :D
     format="DD/MM/YY - hh:mm")
st.write("Início:", start_time)

## aula do dia 9
st.write("##gerando grafico de linhas com dados aleatorios")
import streamlit as st
import pandas as pd
import numpy as np

st.header('Gráfico de linhas')

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

##aula do dia 10
st.write("##selectbox/dropdown")
import streamlit as st

st.header('st.selectbox')

option = st.selectbox(
     'Qual a sua cor favorita?',
     ('Azul', 'Vermelho', 'Verde'))

st.write('Sua cor favorita é ', option)

##aula do dia 11
st.write("##selectbox/dropdown")

import streamlit as st

st.header('st.multiselect')

options = st.multiselect(
     'Quais são suas cores favoritas?',
     ['Verde', 'Amarelo', 'Vermelho', 'Azul'],
     ['Amarelo', 'Vermelho'])

st.write('Você selecionou:', options)

##aula do dia 12
st.write("##checkbox")

import streamlit as st

st.header('st.checkbox')

st.write ('O que você gostaria de pedir?')

icecream = st.checkbox('Sorvete')
coffee = st.checkbox('Café')
cola = st.checkbox('Refrigerante')

if icecream:
     st.write("Sucesso! Aqui está o seu 🍦")

if coffee: 
     st.write("Ok, aqui está o seu café ☕")

if cola:
     st.write("E lá vamos nós 🥤")
     
##aula do dia 13
st.write("##gitpod")

##aulda do dia 14
st.write("https://www.gitpod.io/")

##aula do dia 15
import streamlit as st
st.write("funções")
st.header('st.latex')

st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')

