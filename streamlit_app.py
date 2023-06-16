import numpy as np
import pandas as pd
import streamlit as st
from datetime import time, datetime
#https://streamlit.io/components
#https://echarts.streamlit.app
#https://jrieke-streamlit-analytics-examplessharing-demo-gllu2g.streamlit.app/?analytics=on
st.set_page_config(layout="wide")
# Remove o rodapé padrão
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
# number = st.sidebar.slider('Selecione um número:', 0, 10, 5)
# st.write('O número selecionado no controle deslizante é:', number)


st.markdown(hide_streamlit_style, unsafe_allow_html=True)
# Definir o filtro à esquerda
aula = st.sidebar.selectbox('Selecione a aula',
                            ['Configurando', 'Botão', 'Slider', 'st.line_chart', 'Selectbox', 
                             'Multiselect', 'Checkbox', 'st.latex', 'Customizando', 'st.secrets',
                             'st.file_uploader', 'Layout', 'st.progress', 'st.form'])


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
     st.write("""Componentes são módulos Python desenvolvidos por terceiro que ampliam as possibilidades 
              do Streamlit .https://streamlit.io/components""")
     st.title("15 - st.latex")       
     st.write("st.latex exibe expressões matématicas formatadas como LaTeX.")
     st.title("16 - Customização")
     st.write("""Nós podemos cuistomizar o tema ajustando os parâmetros no arquivo de configuração
              chamado config.toml, que fica dentro da pasta .streamlit, na raiz da aplicação.""")
     st.title("17 - st.secrets")       
     st.write("""st.secrets permite que você armazene informações confidenciais (segredos) como chaves de API, senhas de bancos de dados e outras credenciais.""")
     st.title("18 - st.file_uploader")       
     st.write("st.file_uploader  exibe um componente de upload de arquivo.")
     st.title("19 - Layout")       
     st.write("""Neste tutorial, n'so vamos usar os seguintes comando para definir o layout da sua aplicação Streamlit.
                st.set_page_config(layout="wide") - Exibe os conteúdos da aplicação em modo wide (amplo), caso contrário, por padrão, os conteúdos serão encapsulados em uma caixa com largura fixa.
                st.sidebar - Coloca os componentes, texto e imagens na barra lateral.
                st.expander - Coloca texto e images dentro de uma caixa (container) flexível.
                st.columns - Cria uma coluna onde os conteúdos podem ser adicionados.""")
     st.title("20 - Twitter Space")       
     st.write("Link: https://twitter.com/i/spaces/1dRJZlbglXMKB")
     st.title("20 - st.progress")       
     st.write("st.progress Exite uma barra de progresso, que é atualizada graficamente a medida que iteração progride.")
     st.title("21 - st.form")       
     st.write("""st.form cria um formulário que agrupa os elementos junto com o botão "Enviar".
                Normalmente, quando um usuário interage com um componente a aplicação Streamlit é executada novamente.""")
     
     
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

elif aula == 'st.latex':
     st.header('st.latex')
     import streamlit as st
     
     st.write("funções")
     st.header('st.latex')
     st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')
     st.write("""Uma aplicação simples que exibe uma equação matemática usando sintaxe LaTeX com o comando 
              st.latex.""")

elif aula == 'Customizado':
     st.header('Customizado')
     import streamlit as st

     st.title('Customizando o tema de aplicações Streamlit')

     st.write('Conteúdo do arquivo `.streamlit/config.toml` desta aplicação')

     st.code("""
     [theme]
     primaryColor="#F39C12"
     backgroundColor="#2E86C1"
     secondaryBackgroundColor="#AED6F1"
     textColor="#FFFFFF"
     font="monospace"
     """)

elif aula == 'st.secrets':
     st.header('st.secret')
     st.write("""Explicação linha por linha.A primeira coisa a fazer quando estiver criando uma aplicação
     Strealit é importar a biblioteca streamlit como st:                                               \n
     import streamlit as st                                                                            \n
     Na sequência, vamos adicionar um texto de cabeçalho:                                              \n
     st.title('st.secrets')                                                                            \n
     Finalmente, vamos exibir as informações confidenciais armazenadas:                                \n
     st.write(st.secrets['message'])                                                                   \n
     As informações confidenciais (segredos) podem ser armazenados no Streamlit Cloud como 
     mostrados nas capturas de tela mencionadas abaixo.Caso esteja trabalhando localmente, as 
     informações podem ser armazenadas em .streamlit/secrets.toml, tome muito cuidado para não
     fazer upload desse arquivo para o GitHub quando estiver fazendo um deploy.""")

elif aula == 'st.file_uploader':
     st.header('st.file_uploader')
     import streamlit as st
     import pandas as pd

     st.title('st.file_uploader')

     st.subheader('Upload de CSV')
     uploaded_file = st.file_uploader("Escolha um arquivo")

     if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.subheader('DataFrame')
        st.write(df)
        st.subheader('Estatístiscas descritivas')
        st.write(df.describe())
     else:
        st.info('☝️ Faça upload de um arquivo CSV')
     st.code("""import streamlit as st
     import pandas as pd

     st.title('st.file_uploader')

     st.subheader('Upload de CSV')
     uploaded_file = st.file_uploader("Escolha um arquivo")

     if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.subheader('DataFrame')
        st.write(df)
        st.subheader('Estatístiscas descritivas')
        st.write(df.describe())
     else:
        st.info('☝️ Faça upload de um arquivo CSV')""")

elif aula == 'Layout':
     st.header("Layout")
     import streamlit as st

    #  st.set_page_config(layout="wide")

     st.title('Como customizar o Layout de uma aplicação Streamlit')

     with st.expander('Sobre esta aplicação'):
        st.write('Esta aplicação demonstra diversas maneiras de como você pode definir o layout da sua aplicação Streamlit')
        st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)

     st.sidebar.header('Entrada')
     user_name = st.sidebar.text_input('Qual o seu nome?')
     user_emoji = st.sidebar.selectbox('Escolha um emoji', ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
     user_food = st.sidebar.selectbox('Qual a sua comida favorita?', ['', 'Feijoada', 'Burrito', 'Lasanha', 'Hamburger', 'Pizza'])

     st.header('Saída')

     col1, col2, col3 = st.columns(3)

     with col1:
        if user_name != '':
            st.write(f'👋 Olá {user_name}!')
        else:
            st.write('👈  Por favor escreva seu **nome**!')

     with col2:
        if user_emoji != '':
            st.write(f'{user_emoji} é o seu **emoji** favorito!')
        else:
            st.write('👈 Por favor escolha um **emoji**!')

     with col3:
        if user_food != '':
            st.write(f'🍴 **{user_food}** é a sua **comida** favorita!')
        else:
            st.write('👈 Por favor escolha sua **comida** favorita!')
     st.code("""st.header("Layout")
     import streamlit as st

    #  st.set_page_config(layout="wide")

     st.title('Como customizar o Layout de uma aplicação Streamlit')

     with st.expander('Sobre esta aplicação'):
        st.write('Esta aplicação demonstra diversas maneiras de como você pode definir o layout da sua aplicação Streamlit')
        st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)

     st.sidebar.header('Entrada')
     user_name = st.sidebar.text_input('Qual o seu nome?')
     user_emoji = st.sidebar.selectbox('Escolha um emoji', ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
     user_food = st.sidebar.selectbox('Qual a sua comida favorita?', ['', 'Feijoada', 'Burrito', 'Lasanha', 'Hamburger', 'Pizza'])

     st.header('Saída')

     col1, col2, col3 = st.columns(3)

     with col1:
        if user_name != '':
            st.write(f'👋 Olá {user_name}!')
        else:
            st.write('👈  Por favor escreva seu **nome**!')

     with col2:
        if user_emoji != '':
            st.write(f'{user_emoji} é o seu **emoji** favorito!')
        else:
            st.write('👈 Por favor escolha um **emoji**!')

     with col3:
        if user_food != '':
            st.write(f'🍴 **{user_food}** é a sua **comida** favorita!')
        else:
            st.write('👈 Por favor escolha sua **comida** favorita!')""")

elif aula == 'st.progress':
     import streamlit as st
     import time

     st.title('st.progress')

     with st.expander('Sobre esta aplicação'):
        st.write('Agora você pode exibir o progresso od seus calculosthe progress of your e, uma aplicação Streamlit com o comando `st.progress`.')

     my_bar = st.progress(0)

     for percent_complete in range(100):
        time.sleep(0.05)
        my_bar.progress(percent_complete + 1)

     st.balloons()
     st.code("""import streamlit as st
     import time

     st.title('st.progress')

     with st.expander('Sobre esta aplicação'):
        st.write('Agora você pode exibir o progresso od seus calculosthe progress of your e, uma aplicação Streamlit com o comando `st.progress`.')

     my_bar = st.progress(0)

     for percent_complete in range(100):
        time.sleep(0.05)
        my_bar.progress(percent_complete + 1)

     st.balloons()""")

elif aula == 'st.form':
     st.write("""Um formulário é um container que agrupa visualmente outros elementos e componentes e, 
              também, contém um botão Enviar. Aqui, um usuário pode interagir com um ou mais widgets 
              quantas vezes quiser sem causar uma reexecução. Por fim, quando o botão Enviar do formulário
              é clicado, todos os valores dos componentes, que estão dentro do formulári,o serão enviados
              para o Streamlit de uma vez.
              Para adicionar elementos a um formulário, você pode usar a notação with (preferível) ou 
              pode usá-lo como um objeto, apenas chamando métodos diretamente no formulário (primeiro 
              atribuindo a uma variável e posteriormente aplicando métodos Streamlit). Veja na aplicação de exemplo.

              Os formulários têm algumas restrições:

                Todo formulário deve conter um st.form_submit_button.
                
                st.button e st.download_button não podem ser adicionados a um formulário.
                
                Os formulários podem ser exibidos em qualquer lugar na sua aplicação (barra lateral,
                colunas, etc), mas não podem ser incorporados em outros formulários""")
     import streamlit as st

     st.title('st.form')

     # Exemplo completo usando a notação with
     st.header('1. Exemplo usando a notação `with`')
     st.subheader('Cafeteira')

     with st.form('my_form'):
         st.subheader('**Escolha seu café**')

         # Componentes de entrada
         coffee_bean_val = st.selectbox('Grão', ['Arabica', 'Robusta'])
         coffee_roast_val = st.selectbox('Torra', ['Clara', 'Média', 'Escura'])
         brewing_val = st.selectbox('Método', ['Aeropress', 'Filtrado', 'Prensa Francesa', 'Cafeteira Italiana', 'Globo'])
         serving_type_val = st.selectbox('Formato', ['Quente', 'Gelado', 'Frapê'])
         milk_val = st.select_slider('Leite', ['Não', 'Pouco', 'Médio', 'Muito'])
         owncup_val = st.checkbox('Trouxe o meu copo!') 

         # Todo formulário deve ter um botão enviar
         submitted = st.form_submit_button('Enviar')

     if submitted:
        st.markdown(f'''
            ☕ Você pediu:
            - Grão: `{coffee_bean_val}`
            - Torra: `{coffee_roast_val}`
            - Método: `{brewing_val}`
            - Formato: `{serving_type_val}`
            - Leite: `{milk_val}`
            - Trouxe o meu copo: `{owncup_val}`
            ''')
     else:
         st.write('☝️ Faça o seu pedido!')


     # Pequeno exemplo usando objeto
     st.header('2. Exemplo com objeto')

     form = st.form('my_form_2')
     selected_val = form.slider('Escolha um valor')
     form.form_submit_button('Enviar')

     st.write('Valor escolhido: ', selected_val)
     st.code("""     import streamlit as st

     st.title('st.form')

     # Exemplo completo usando a notação with
     st.header('1. Exemplo usando a notação `with`')
     st.subheader('Cafeteira')

     with st.form('my_form'):
         st.subheader('**Escolha seu café**')

         # Componentes de entrada
         coffee_bean_val = st.selectbox('Grão', ['Arabica', 'Robusta'])
         coffee_roast_val = st.selectbox('Torra', ['Clara', 'Média', 'Escura'])
         brewing_val = st.selectbox('Método', ['Aeropress', 'Filtrado', 'Prensa Francesa', 'Cafeteira Italiana', 'Globo'])
         serving_type_val = st.selectbox('Formato', ['Quente', 'Gelado', 'Frapê'])
         milk_val = st.select_slider('Leite', ['Não', 'Pouco', 'Médio', 'Muito'])
         owncup_val = st.checkbox('Trouxe o meu copo!') 

         # Todo formulário deve ter um botão enviar
         submitted = st.form_submit_button('Enviar')

     if submitted:
        st.markdown(f'''
            ☕ Você pediu:
            - Grão: `{coffee_bean_val}`
            - Torra: `{coffee_roast_val}`
            - Método: `{brewing_val}`
            - Formato: `{serving_type_val}`
            - Leite: `{milk_val}`
            - Trouxe o meu copo: `{owncup_val}`
            ''')
     else:
         st.write('☝️ Faça o seu pedido!')


     # Pequeno exemplo usando objeto
     st.header('2. Exemplo com objeto')

     form = st.form('my_form_2')
     selected_val = form.slider('Escolha um valor')
     form.form_submit_button('Enviar')

     st.write('Valor escolhido: ', selected_val)
     """)
