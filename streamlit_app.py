import streamlit as st

# st.header('st.button')

# if st.button('Say hello'):
#      st.write('Why hello there')
# else:
#      st.write('Goodbye')
     
     
 ## BUTÃO    
# st.title("make a button")

# result = st.button("click here")

# st.write(result)

# if result:
#      st.write(":smile:")
     
# st.title("checkbox")

### Botão check, checkbox, botão

# ## check button 
# st.title("buttonchecks, checkboxes and buttons")

# page_names = ["Checkbox", "Button"]
# page = st.radio('Navegation', page_names)
# st.write("**The variable 'page' returns:**", page)

# ## buttoncheck
# if page == "Checkbox":
#      st.subheader("welcome to the checkbox page!")
#      st.write("nice to see you! :wave:")
#      check = st.checkbox("click here")
#      st.write('state of the checkbox', check)
     
# if check:
#      nested_btn = st.button("button nested in Checkbox")
     
#      if nested_btn:
#           st.write(":cake:"*10)         
# else:
#      st.subheader("welcome to the button page!")
#      st.write(":thumbsup")
#      result = st.button("Click Here")
#      st.write("state of button:", result)
     
# if result:
#      nested_check = st.checkbox("Checkbox nested in button")
     
#      if nested_check:
#           st.write(":heart:"*10)
     
     
## aula  do dia 8
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
     format="DD/MM/YY - hh:mm")
st.write("Início:", start_time)