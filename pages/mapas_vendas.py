import streamlit as st
import pandas as pd
import plotly.express as px
from numpy.random import default_rng as rng
import pydeck as pdk

dados_vendas = pd.read_csv("dados/vendas_geolocalizacao.csv")
st.title("🗺️ Mapas de vendas por Região")
dados_filtrados = dados_vendas[dados_vendas['Vendas']>0].copy()
st.dataframe(dados_filtrados.head())
col1,col2,col3,col4 = st.columns(4)
with col1:
    qpv_Q_linha = dados_filtrados['Vendas'].sum()
    st.metric(label='quantidade de pontos de venda',value=f'{qpv_Q_linha} somados')
with col2:
    quantidade_cidade = dados_filtrados['Cidade']
    st.metric(label='cidades que realizarao as vendas',value=f'{quantidade_cidade}')
with col3:
  soma_vendas = dados_filtrados['Vendas'].sum()
  st.metric(label='soma das vendas realizadas',value=format(soma_vendas))  
with col4:
  soma_lucro = dados_filtrados['Lucro'].sum()
  st.metric(label='soma dos lucros',value=format(soma_lucro))  

dados_vendas = pd.read_csv(
    "dados/vendas_geolocalizacao.csv",
    usecols=["Latitude", "Longitude","Região", "Cidade", "Vendas", "Lucro"],
    sep=",",encoding="utf-8"
)
dados_vendas["Latitude"]=pd.to_numeric(dados_vendas["Latitude"],errors="coerce")
dados_vendas["Longitude"]=pd.to_numeric(dados_vendas["Longitude"],errors="coerce")
st.map(dados_vendas,latitude="Latitude",longitude="Longitude")

st.dataframe(dados_filtrados)
