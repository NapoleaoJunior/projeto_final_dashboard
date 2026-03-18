import streamlit as st
import pandas as pd
import plotly.express as px

dados_vendas = pd.read_csv("dados/dados_vendas.csv")
st.title("💰analise de produtos - professor")

# armazena na memoria a opcao selecionada
opcao = st.selectbox(
    "selecione  um produto",
    ("headset", "teclado", "mouse", "notebook", "ssd", "monitor")
)

#quero filtrar os dados de venda usando a opcao selecionada
dados_filtrados = dados_vendas[dados_vendas['produto']==opcao]
st.dataframe(dados_filtrados.head())
col1, col2, col3, col4 = st.columns(4)

with col1:
    receita=dados_filtrados['vendas'].sum()
    st.metric(label="receita", value=f'R$ {receita:,.2f}')

with col2:
    lucro=dados_filtrados['lucro'].sum()
    st.metric(label="lucro", value=f'R$ {lucro:,.2f}')

with col3:
    quantidade=dados_filtrados['quantidade'].sum()
    st.metric(label="quantidade vendida", value=f'{quantidade} unidades')

with col4:
    preco_medio=receita/quantidade
    st.metric(label="preco medio", value=f'R$ {preco_medio:,.2f}')