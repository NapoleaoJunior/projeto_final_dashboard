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
    st.metric('quantidade de pontos de venda',dados_filtrados.shape[0])
with col2:
    st.metric('cidades que realizarao as vendas',dados_filtrados["Cidade"].nunique())
with col3:
  st.metric('soma das vendas realizadas',f"R$ {dados_filtrados['Vendas'].sum():,.2f}")  
with col4:
  st.metric('soma dos lucros',f"R$ {dados_filtrados['Lucro'].sum():,.2f}")  

dados_vendas = pd.read_csv(
    "dados/vendas_geolocalizacao.csv",
    usecols=["Latitude", "Longitude","Região", "Cidade", "Vendas", "Lucro"],
    sep=",",encoding="utf-8"
)
dados_vendas["Latitude"]=pd.to_numeric(dados_vendas["Latitude"],errors="coerce")
dados_vendas["Longitude"]=pd.to_numeric(dados_vendas["Longitude"],errors="coerce")
st.map(dados_vendas,latitude="Latitude",longitude="Longitude")

st.dataframe(dados_filtrados)
