import streamlit as st
import pandas as pd
import plotly.express as px

def carregar_dados():
    #carregar dados de vendas
    df = pd.read_csv('dados/dados_vendas.csv')
    return df
dados_vendas = carregar_dados()

st.title("visao geral do negocio")
#KPIS principal
col1,col2,col3,col4 = st.columns(4)
col1.metric(":moneybag: receita total",f"R$ {dados_vendas['vendas'].sum():,.2f}")
col2.metric(":chart_with_upwards_trend: lucro total",f"R$ {dados_vendas['lucro'].sum():,.2f}")
col3.metric(":shopping_cart: total transacoes",f"{len(dados_vendas)}")
col4.metric(":bar_chart: ticket medio",f"R$ {dados_vendas['vendas'].mean():,.2f}")

st.divider()
#graficos de resumos
colA,colB = st.columns(2)
with colA:
    vendas_regiao = dados_vendas.groupby('regiao')['vendas'].sum().reset_index()
    fig = px.pie(vendas_regiao,names='regiao',values='vendas',
                 title='distribuicao de vendas por regiao',hole=0.4)
    st.plotly_chart(fig,width='stretch')

with colB:
    dados_vendas['data']= pd.to_datetime(dados_vendas['data'])
    dados_vendas['mes']=dados_vendas['data'].dt.to_period('m').astype(str)
    vendas_mensal = dados_vendas.groupby('mes')['vendas'].sum().reset_index()
    fig = px.line(vendas_mensal,x='mes',y='vendas',title='evolucao mensal',markers=True)
    st.plotly_chart(fig,width='stretch')

st.subheader(":moneybag: top 5 produtos por receita")
top5_produtos = dados_vendas.groupby('produto')['vendas'].sum().nlargest(5).reset_index()
fig = px.bar(top5_produtos,x='produto',y='vendas',title='top 5 produtos',
             color='vendas',color_continuous_scale='peach')
st.plotly_chart(fig,width='stretch')