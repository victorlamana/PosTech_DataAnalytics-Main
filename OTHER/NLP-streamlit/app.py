import streamlit as st
import spacy
import matplotlib.pyplot as plt

# Carregar o modelo spaCy
nlp = spacy.load("pt_core_news_sm")

# Função para extrair entidades manualmente
def extrair_entidades(texto):
    doc = nlp(texto)
    estudantes = []
    anos = []
    tokens = [token.text for token in doc]
    i = 0
    while i < len(tokens):
        if tokens[i].lower() == "estudante":
            if i + 1 < len(tokens) and tokens[i + 1].isdigit():
                estudantes.append(f"{tokens[i].lower()} {tokens[i + 1]}")
                i += 1  # Pular o próximo token, pois já foi usado
        elif tokens[i].isdigit() and len(tokens[i]) == 4:
            anos.append(tokens[i])
        i += 1
    return estudantes, anos

# Dados de exemplo para visualização
dados = {
    "estudante 1": {"2020": 75, "2021": 85, "2022": 90},
    "estudante 2": {"2020": 80, "2021": 78, "2022": 88}
}

# App Streamlit
st.title("Visualização de Dados dos Estudantes")

# Solicitar entrada do usuário
entrada_usuario = st.text_input("Digite seu prompt (ex.: 'dados do estudante 1', 'comparar estudante 1 e 2 em 2020')")

if entrada_usuario:
    estudantes, anos = extrair_entidades(entrada_usuario)

    if "comparar" in entrada_usuario:
        if len(estudantes) == 2 and len(anos) == 1:
            estudante1, estudante2 = estudantes
            ano = anos[0]

            if estudante1 in dados and estudante2 in dados and ano in dados[estudante1] and ano in dados[estudante2]:
                valores = [dados[estudante1][ano], dados[estudante2][ano]]

                fig, ax = plt.subplots()
                ax.bar([estudante1, estudante2], valores, color=['blue', 'green'])
                ax.set_ylabel('Pontuações')
                ax.set_title(f'Comparação entre {estudante1} e {estudante2} em {ano}')
                st.pyplot(fig)
            else:
                st.error("Estudantes ou ano inválidos.")
        else:
            st.error("Por favor, forneça exatamente dois estudantes e um ano.")
    else:
        if len(estudantes) == 1:
            estudante = estudantes[0]
            if estudante in dados:
                anos_estudante = list(dados[estudante].keys())
                pontuacoes = list(dados[estudante].values())

                fig, ax = plt.subplots()
                ax.plot(anos_estudante, pontuacoes, marker='o', linestyle='-', color='blue')
                ax.set_ylabel('Pontuações')
                ax.set_title(f'Dados do {estudante}')
                st.pyplot(fig)
            else:
                st.error("Estudante inválido.")
        else:
            st.error("Por favor, forneça exatamente um estudante.")
