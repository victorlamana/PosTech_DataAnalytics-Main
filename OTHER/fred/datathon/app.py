import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Visão 360 Aluno",
    layout="wide",
    initial_sidebar_state="expanded",
)

df = pd.read_csv('dados_finais.csv')

def obter_dados_e_previsao(id_aluno):
    df_aluno = df[df['ID_ALUNO'] == id_aluno].sort_values(by='ANO_PESQUISA')
    if df_aluno.empty:
        return None, None, None

    serie_temporal = df_aluno['INDE'].values
    anos = df_aluno['ANO_PESQUISA'].values
    return serie_temporal, anos


def plotar_grafico_inde(serie_temporal, anos, id_aluno):
    plt.figure(figsize=(10, 5))

    anos_predicao = list(anos) + [max(anos) + 1]
    valores_com_predicao = list(serie_temporal)

    plt.plot(anos, serie_temporal, marker='o', linestyle='-', label='INDE Real', color='b')

    plt.legend()
    st.pyplot(plt)



def pagina_previsao():
    st.title('Previsão do INDE para Alunos')

    id_aluno = st.text_input('Insira o ID do aluno:', '')

    if id_aluno:
        try:
            id_aluno_int = int(id_aluno)
            serie_temporal, anos = obter_dados_e_previsao(id_aluno_int)
            if serie_temporal is not None:
                st.subheader(f'O INDE previsto para o aluno {id_aluno_int} é:')
                st.markdown("##")
                plotar_grafico_inde(serie_temporal, anos, id_aluno_int)
            else:
                st.write('ID do aluno não encontrado.')
        except ValueError:
            st.write('Por favor, insira um ID válido.')


def pagina_sobre_modelo():
    st.title('Modelo de Previsão do INDE')
    # st.image('imagem2.jpg', width=500)
    st.subheader('**Por que escolher o INDE?**')
    st.write('''
        Com base no dataset fornecido, percebemos que o INDE é uma das medidas mais relevantes para o aluno e para a ONG como um todo. Ele mostra o desenvolvimento do aluno de forma global, incluindo aspectos psicossociais e acadêmicos, além de ser uma medida prática para mensurar a variação do rendimento do aluno em anos distintos. Por isso, optamos por usá-la como base do nosso modelo. 
    ''')
    st.subheader('**O modelo**')
    st.write('''
        Considerando o INDE como a principal medida do rendimento dos alunos, refletimos sobre as vantagens de se ter um modelo que consiga prever o INDE antes do final do período letivo, com base nos índices de anos anteriores. Pensamos que a previsão do INDE pode ser relevante para fornecer mais apoio e atenção extra aos alunos com índices previstos mais baixos, para que a situação ainda possa ser mudada ao longo do período letivo e para que o aluno tenha chance de aumentar seu INDE no processo. 
    ''')

    st.subheader('**Os dados**')
    st.write('''
        Para criar o modelo, consideramos o dataset como sendo uma série temporal de cada aluno. Diversos alunos não tem os INDEs registrados nos 3 anos contidos no dataset, portanto, para preservar a profundidade da série temporal, consideramos somente os alunos que tinham INDEs registrados em 2020, 2021 e 2022, totalizando 314 alunos. Entendemos que a quantidade de dados fornecidos não é a ideal para treinar o modelo, mas essa pode ser uma primeira versão para inspirar a criação de um modelo mais robusto com o aumento de dados futuro.
    ''')
    st.subheader('**Validação**')
    st.write('''
        Para validar e analisar o desempenho do modelo, utilizamos as seguintes medidas: Erro Quadrático Médio, Raiz do Erro Quadrático Médio, Erro Absoluto Médio e Coeficiente de Determinação. Sabemos que os resultados podem ser aprimorados com uso de uma base de dados mais robusta e com índices de novos alunos e novos anos.
            
            MSE: 0.5757492888524077
            RMSE: 0.7587814499922937
            MAE: 0.4959931007463785
            R²: 0.5283160916027065
        ''')

pagina = st.sidebar.selectbox('Escolha uma página:', ['Sobre o modelo', 'Previsão INDE'])

if pagina == 'Sobre o modelo':
    pagina_sobre_modelo()
elif pagina == 'Previsão INDE':
    pagina_previsao()




#%%
