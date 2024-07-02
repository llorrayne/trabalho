import streamlit as st
import requests

st.title('Gerenciador de Cep')

st.markdown('Digite os dados a seguir: Nome, Telefone, e-mail, CPF e CEP...')

cep = st.text_input(
    label='Digite um cep',
    placeholder='Somente números'
    )

try:
    endereco = requests.get('https://viacep.com.br/ws/{cep}/json/').json()
except:
   st.error('Deu erro')
st.write(endereco)
