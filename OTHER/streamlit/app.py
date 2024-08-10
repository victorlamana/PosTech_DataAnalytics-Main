import streamlit as st
from pages import previsao, sobre_modelo, filtrar_dataframe, home

st.set_page_config(
    page_title="Vis�o 360 Aluno",
    layout="wide",
    initial_sidebar_state="expanded",
)

pagina = st.sidebar.selectbox('Escolha uma p�gina:', ['Home', 'Sobre o modelo', 'Previs�o INDE', 'Filtrar DataFrame'])

if pagina == 'Home':
    home.mostrar()
elif pagina == 'Sobre o modelo':
    sobre_modelo.mostrar()
elif pagina == 'Previs�o INDE':
    previsao.mostrar()
elif pagina == 'Filtrar DataFrame':
    filtrar_dataframe.mostrar()