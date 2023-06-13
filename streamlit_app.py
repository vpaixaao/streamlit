import numpy as np
import pandas as pd
import streamlit as st
from datetime import time, datetime


st.set_page_config(layout="wide")
# Remove o rodapé padrão
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
# Definir o filtro à esquerda
aula = st.sidebar.selectbox('Selecione a aula',
                            ['Configurando', 'Botão', 'Slider', 'Gráfico de linhas', 'Selectbox', 
                             'Multiselect', 'Checkbox', 'Gitpod', 'Config', 'File Uploader'])

if aula == "Configurando":
     st.title("01 - Configurando ")
     st.write("Instalar o conda: https://docs.conda.io/en/latest/miniconda.html ")
     st.write("no cmd -> pip install streamlit")
     st.write("streamlit hello")
     st.title("02 - Abrindo ")
     st.write("no terminal escreva: streamlit run NOME-DO-ARQUIVO.py ")
     st.title("03 - Botão ")
     st.write("Como criar um botão")
     st.title("04 - Resumão")
     st.write("exemplo de construção de app com o STREAMLIT: https://www.youtube.com/c/KenJee1")
     st.title("05 - st.write")
     st.write("""print do streamlit                                                                     
               ele pode imprimir: strings, dicionarios, dataframes, plotar graficos....                           
               (https://docs.streamlit.io/library/api-reference/write-magic/st.write)""")
     st.title("06 - Github")
     st.write("""Repositório GitHub                                                                     
               Siga os seguintes passos para criar um repositório no GitHub:                                      
               No canto superior direito, click no ícone "+" que mostrará um menu, então clique em 
               "New repository".Isso vai abrir uma nova página "Create a new repository". No campo 
               "Repository name", escolha um nome para o seu repositório, por exemplo, helloworld.
               Na parte "Initialize this repository with:", marque a opção"Add a README file". 
               Finalmente, clique em "Create repository". Seu novo repositório estará disponível 
               em https://github.com/dataprofessor/helloworld e dataprofessor é o seu nome de
               usuário e helloworld é o nome do repositório.""")               
     st.title("07 - Fazendo deploy ")
     st.write("""Streamlit Cloud Streamlit Cloud é um serviço de hospedagem que facilita o deploy 
               de aplicações Streamlit. Criando a sua conta Streamlit Cloud. Você pode criar sua 
               conta no Streamlit Cloud simplesmente se logando com sua conta Google ou GitHub. 
               Fazendo deploy da sua aplicação Streamlit. Para fazer deploy de uma aplicação Streamlit,                                                                                     
               siga os seguintes passos: To deploy, a Streamlit app, do the following: Faça login com 
               sua conta GitHub ou Gmail. Escolha um reposiório, branch e arquivo. Clique em Deploy.
               Agora, sempre que você fizer um git push (enviar arquivos, da sua aplicação, ao seu
               repositório) sua aplicação atualizará automaticamente. """) 
     st.title("08 - Slider")       
     st.write("Como construir um slider")                    
     st.write("""st.line_chart permite exibir um gráfico de linhas
               Este é um açúcar sintático relacionado ao st.altair_chart. A principal diferença
               é que este comando usa as colunas e índices dos próprios dados e tenta descobrir a
               melhora maneira de exibir o gráfico. Ou seja, é mais fácil de usar para os cenários
               "apenas exiba o gráfico", porém menos customizável. Se o st.line_chart não acertar
               a melhor maneira de exibir o gráfico, ou o melhor tipo, tente usar o st.altair_chart
               e especifique a informação desejada.""")        
     st.title("09 - st.line_chart")       
     st.write("""st.line_chart permite exibir um gráfico de linha. Este é um açúcar                      
               sintático relacionado ao st.altair_chart. A principal diferença é que este comando                  
               usa as colunas e índices dos próprios dados e tenta descobrir a melhora maneira de                   
               exibir o gráfico. Ou seja, é mais fácil de usar para os cenários "apenas exiba o                    
               gráfico", porém menos customizável.Se o st.line_chart não acertar a melhor maneira                  
               de exibir o gráfico, ou o melhor tipo, tente usar o st.altair_chart e especifique                   
               a informação desejada.""")
     st.title("10 - st.selectbox")       
     st.write("Caixa de seleção")
     st.title("11 - st.multiselect")       
     st.write("Caixa de multiplas seleções")
     st.title("12 - st.checkbox")       
     st.write("Caixa de checagem")
     st.title("13 - Gitpod")       
     st.write("""Para subir um ambiente de desenvolvimento na nuvem, nós podemos usar o GitPod e é só 
                clicar no seguinte link: https://gitpod.io/#/https://github.com/dataprofessor/streamlit101/
                Como você pode ver na URL acima, a URL do repositório no GitHub é adicionada depois de 
                https://gitpod.io/#/ o que permite o GitPod subir um ambiente de desenvolvimento usado
                as instruções contidas na URL do repositório GitHub (neste caso o arquivo requirements.
                txt que especifica quais bibliotecas Python devem ser instaladas).
                Observação: Existem outros ambientes de desenvolvimento na nuvem semelhantes:\n
                GitHub Codespaces \n https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/setting-up-your-python-project-for-codespaces \n
                Replit \n https://replit.com/\n
                Cloud9 \n https://aws.amazon.com/cloud9/""")
     st.title("14 - Components")
     st.write("")     
     
elif aula == 'Botão':
     st.title("03 - Criando um botão")
     result = st.button("Clique aqui")
     st.write(result)
     if result:
        st.write(":smile:")
     st.write(""".
                st.title("03 - Criando um botão")  
                result = st.button("Clique aqui")               
                st.write(result)                                
                if result:                                      
                st.write(":smile:")                             
                """)
    
elif aula == 'Slider':
     st.header('08 - st.slider')    
     st.write(""".             
    st.slider permite exibir um controle deslizante (slider).
    Os seguintes tipos do Python são suportados: int, float, date, time, and datetime.""")
  
     st.subheader('Exemplo 1 - Slider')
     age = st.slider('Quantos anos você tem?', 0, 130, 25)
     st.write("Eu tenho ", age, ' anos')
     st.write(""".
      
    age = st.slider('Quantos anos você tem?', 0, 130, 25)  
         
    st.write("Eu tenho ", age, ' anos')""")

     st.subheader('Exemplo 2 - Slider de intervalo')
     values = st.slider('Escolha um intervalo de valores', 0.0, 100.0, (25.0, 75.0))
     st.write('Valores:', values)
     st.write(""".
      
       values = st.slider( 
       'Escolha um intervalo de valores',     
       0.0, 100.0, (25.0, 75.0))
       
       st.write('Valores:', values)
       """)

     st.subheader('Slider de intervalo de tempo')
     appointment = st.slider("Agende um compromisso:", value=(time(11, 30), time(12, 45)))
     st.write("O compromisso foi agendado para:", appointment)
     st.write(""".
              
    appointment = st.slider(         
    "Agende um compromisso:",        
    value=(time(11, 30), time(12, 45))) 
            
    st.write("O compromisso foi agendado para:", appointment)""")

     st.subheader('Slider de data e hora')
     start_time = st.slider("Quando você vai começar?", value=datetime(2020, 1, 1, 9, 30), format="DD/MM/YY - hh:mm")
     st.write("Início:", start_time)
     st.write(""".
              
    start_time = st.slider(          
    "Quando você vai começar?",
    value=datetime(2020, 1, 1, 9, 30),
    format="MM/DD/YY - hh:mm")
    st.write("Início:", start_time)""")
   
elif aula == 'st.line_chart':
     st.header('Gráfico de linhas')
     chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
     st.line_chart(chart_data)
     st.write(""".
              
    import streamlit as st
    import pandas as pd
    import numpy as np

    st.header('Gráfico de linhas')

    chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

    st.line_chart(chart_data)""")

elif aula == 'Selectbox':
     st.header('st.selectbox')
     option = st.selectbox('Qual a sua cor favorita?', ('Azul', 'Vermelho', 'Verde'))
     st.write('Sua cor favorita é', option)
     st.write(""".
              
    import streamlit as st
    st.header('st.selectbox')

    option = st.selectbox(
    'Qual a sua cor favorita?',
    ('Azul', 'Vermelho', 'Verde'))""")

elif aula == 'Multiselect':
     st.header('st.multiselect')
     options = st.multiselect('Quais são suas cores favoritas?', ['Verde', 'Amarelo', 'Vermelho', 'Azul'], ['Amarelo', 'Vermelho'])
     st.write('Você selecionou:', options)
     st.write(""".
                          
    import streamlit as st
    
    st.header('st.multiselect')
    
    options = st.multiselect(
    'Quais são suas cores favoritas?',
    ['Verde', 'Amarelo', 'Vermelho', 'Azul'],
    ['Amarelo', 'Vermelho'])
    
    st.write('Você selecionou:', options)""")

elif aula == 'Checkbox':
     st.header('st.checkbox')
     st.write('O que você gostaria de pedir?')
     icecream = st.checkbox('Sorvete')
     coffee = st.checkbox('Café')
     cola = st.checkbox('Refrigerante')
     if icecream:
        st.write("Sucesso! Aqui está o seu 🍦")
     if coffee: 
        st.write("Ok, aqui está o seu café ☕")
     if cola:
        st.write("E lá vamos nós 🥤")
     st.write(""".
              
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
        st.write("E lá vamos nós 🥤") """)

elif aula == 'Components':
    st.write("")











# import streamlit as st

# ## Botão    
# st.title("Criando um botão")

# result = st.button("click here")

# st.write(result)

# if result:
#      st.write(":smile:")
     
# # aula  do dia 8
# import streamlit as st
# from datetime import time, datetime

# st.header('st.slider')

# # Exemplo 1

# st.subheader('Slider')

# age = st.slider('Quantos anos você tem?', 0, 130, 25)
# st.write("Eu tenho ", age, ' anos')

# # Exemplo 2

# st.subheader('Slider de intervalo')

# values = st.slider(
#      'Escolha um intervalo de valores',
#      0.0, 100.0, (25.0, 75.0))
# st.write('Valores:', values)

# # Exemplo 3

# st.subheader('Slider de intervalo de tempo')

# appointment = st.slider(
#      "Agende um compromisso:",
#      value=(time(11, 30), time(12, 45)))
# st.write("O compromisso foi agendado para:", appointment)

# # Exemplo 4

# st.subheader('Slider de data e hora')

# start_time = st.slider(
#      "Quando você vai começar?",
#      value=datetime(2020, 1, 1, 9, 30),
#      ## só formatar o tipo de data :D
#      format="DD/MM/YY - hh:mm")
# st.write("Início:", start_time)

# ## aula do dia 9
# st.write("##gerando grafico de linhas com dados aleatorios")
# import streamlit as st
# import pandas as pd
# import numpy as np

# st.header('Gráfico de linhas')

# chart_data = pd.DataFrame(
#      np.random.randn(20, 3),
#      columns=['a', 'b', 'c'])

# st.line_chart(chart_data)

# ##aula do dia 10
# st.write("##selectbox/dropdown")
# import streamlit as st

# st.header('st.selectbox')

# option = st.selectbox(
#      'Qual a sua cor favorita?',
#      ('Azul', 'Vermelho', 'Verde'))

# st.write('Sua cor favorita é ', option)

# ##aula do dia 11
# st.write("##selectbox/dropdown")

# import streamlit as st

# st.header('st.multiselect')

# options = st.multiselect(
#      'Quais são suas cores favoritas?',
#      ['Verde', 'Amarelo', 'Vermelho', 'Azul'],
#      ['Amarelo', 'Vermelho'])

# st.write('Você selecionou:', options)

# ##aula do dia 12
# st.write("##checkbox")

# import streamlit as st

# st.header('st.checkbox')

# st.write ('O que você gostaria de pedir?')

# icecream = st.checkbox('Sorvete')
# coffee = st.checkbox('Café')
# cola = st.checkbox('Refrigerante')

# if icecream:
#      st.write("Sucesso! Aqui está o seu 🍦")

# if coffee: 
#      st.write("Ok, aqui está o seu café ☕")

# if cola:
#      st.write("E lá vamos nós 🥤")
     
# ##aula do dia 13
# st.write("##gitpod")

# ##aulda do dia 14
# st.write("https://www.gitpod.io/")

# ##aula do dia 15
# import streamlit as st
# st.write("funções")
# st.header('st.latex')

# st.latex(r'''
#      a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
#      \sum_{k=0}^{n-1} ar^k =
#      a \left(\frac{1-r^{n}}{1-r}\right)
#      ''')

# ##aula do dia 16
# import streamlit as st

# st.title('Customizando o tema de aplicações Streamlit')

# st.write('Conteúdo do arquivo `.streamlit/config.py` desta aplicação')

# st.code("""
# [theme]
# primaryColor="#FF0000"
# backgroundColor="#FF0000"
# secondaryBackgroundColor="#FF0000"
# textColor="#FFFFFF"
# font="monospace"
# """)

# ## criação do menu lateral =)

# number = st.sidebar.slider('Selecione um número:', 0, 10, 5)
# st.write('O número selecionado no controle deslizante é:', number)

# ##aula do dia 17

# import streamlit as st

# st.title('st.secrets')

# # st.write(st.secrets['message'])

# ##aula do dia 18

# import streamlit as st
# import pandas as pd

# st.title('st.file_uploader')

# st.subheader('Upload de CSV')
# uploaded_file = st.file_uploader("Escolha um arquivo")

# if uploaded_file is not None:
#   df = pd.read_csv(uploaded_file)
#   st.subheader('DataFrame')
#   st.write(df)
#   st.subheader('Estatístiscas descritivas')
#   st.write(df.describe())
# else:
#   st.info('☝️ Faça upload de um arquivo CSV')

##aula do dia 19

# import streamlit as st

# st.set_page_config(layout="wide")

# st.title('Como customizar o Layout de uma aplicação Streamlit')

# with st.expander('Sobre esta aplicação'):
#   st.write('Esta aplicação demonstra diversas maneiras de como você pode definir o layout da sua aplicação Streamlit')
#   st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)

# st.sidebar.header('Entrada')
# user_name = st.sidebar.text_input('Qual o seu nome?')
# user_emoji = st.sidebar.selectbox('Escolha um emoji', ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
# user_food = st.sidebar.selectbox('Qual a sua comida favorita?', ['', 'Feijoada', 'Burrito', 'Lasanha', 'Hamburger', 'Pizza'])

# st.header('Saída')

# col1, col2, col3 = st.columns(3)

# with col1:
#   if user_name != '':
#     st.write(f'👋 Olá {user_name}!')
#   else:
#     st.write('👈  Por favor escreva seu **nome**!')

# with col2:
#   if user_emoji != '':
#     st.write(f'{user_emoji} é o seu **emoji** favorito!')
#   else:
#     st.write('👈 Por favor escolha um **emoji**!')

# with col3:
#   if user_food != '':
#     st.write(f'🍴 **{user_food}** é a sua **comida** favorita!')
#   else:
#     st.write('👈 Por favor escolha sua **comida** favorita!')


##aula do dia 20
##aula do dia 21
##aula do dia 22
##aula do dia 23
##aula do dia 24
##aula do dia 25
##aula do dia 26
##aula do dia 27
##aula do dia 28
##aula do dia 29
##aula do dia 30
