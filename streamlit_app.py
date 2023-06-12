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

## check button 
st.title("buttonchecks, checkboxes and buttons")

page_names = ["Checkbox", "Button"]
page = st.radio('Navegation', page_names)
st.write("**The variable 'page' returns:**", page)

## buttoncheck
if page == "Checkbox":
     st.subheader("welcome to the checkbox page!")
     st.write("nice to see you! :wave:")
     check = st.checkbox("click here")
     st.write('state of the checkbox', check)
     
if check:
     nested_btn = st.button("button nested in Checkbox")
     
     if nested_btn:
          st.write(":cake:"*10)         
else:
     st.subheader("welcome to the button page!")
     st.write(":thumbsup")
     result = st.button("Click Here")
     st.write("state of button:", result)
     
if result:
     nested_check = st.checkbox("Checkbox nested in button")
     
     if nested_check:
          st.write(":heart:"*10)
     