# notebook_page.py
import streamlit as st
import streamlit.components.v1 as components


st.title("Embedded Notebook")

# Path to your HTML file
html_file_path = 'DATATHON_PREPARACAO.html'

# Display the HTML content in an iframe
st.markdown(f"""
    <iframe src="{html_file_path}" style="width:100%; height:1200px; border:none;"></iframe>
""", unsafe_allow_html=True)