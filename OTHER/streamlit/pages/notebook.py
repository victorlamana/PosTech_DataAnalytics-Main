# notebook_page.py
import streamlit as st
import streamlit.components.v1 as components


st.title("Embedded Notebook")

# Path to your HTML file
html_file_path = 'DATATHON_PREPARACAO.html'

# Read the HTML file
with open(html_file_path, 'r') as f:
    html_content = f.read()

# Display the HTML content in Streamlit
components.html(html_content, height=800)