import streamlit as st
import pandas as pd
import plotly.express as px

def carregar_dados():
    df = pd.read_csv('dados/dados_vendas.csv')
    df['data']=pd.to_datetime(df['data'])
    return df
dado_vendas = carregar_dados()
st.title(':moneybag: analise detalhada de vendas')
st.sidebar.header("filtros de vendas")
