import streamlit as st
import pandas as pd
import plotly.express as px
import locale

# Função para formatar valores em reais
 
def format_brl(value):
    # Set the locale to Brazilian Portuguese
    # On some systems, the locale string might be slightly different (e.g., 'pt_BR.UTF-8')
    try:
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    except locale.Error:
        # Fallback for systems where 'pt_BR.UTF-8' is not available
        try:
            locale.setlocale(locale.LC_ALL, 'pt_BR')
        except locale.Error:
            print("Warning: Could not set pt_BR locale. Falling back to simple formatting.")
            return f"R$ {value:,.2f}".replace('.', 'X').replace(',', '.').replace('X', ',')
 
    # Format the value as currency with grouping enabled
    # locale.currency() returns a string like 'R$ 1.234,56'
    formatted_value = locale.currency(value, symbol=True, grouping=True)
    return formatted_value

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
    st.metric(label="receita", value=format_brl (receita))

with col2:
    lucro=dados_filtrados['lucro'].sum()
    st.metric(label="lucro", value=format_brl(lucro))

with col3:
    quantidade=dados_filtrados['quantidade'].sum()
    st.metric(label="quantidade vendida", value=f'{quantidade} unidades')

with col4:
    preco_medio=receita/quantidade
    st.metric(label="preco medio", value=format_brl(preco_medio))

colA,colB = st.columns(2)
with colA:
    df_agrupado = dados_filtrados.groupby('região')['vendas'].sum().reset_index()
    fig = px.bar(df_agrupado,x='região',y='vendas'
                 ,title=f'vendas por regiao - {opcao}',color='vendas')
    st.plotly_chart(fig,width='stretch')
with colB:
    vendedor_vendas = dados_filtrados.groupby('vendedor')['vendas'].sum().reset_index()
    fig = px.pie(vendedor_vendas,values='vendas',names='vendedor',title='vendas por vendedor')
    st.plotly_chart(fig,width='stretch')

#criando a coluna mes
dados_filtrados['data']=pd.to_datetime(dados_filtrados['data'])
dados_filtrados['mes']=dados_filtrados['data'].dt.to_period('M').astype(str)
st.dataframe(dados_filtrados.head())
df_agrupado3 = dados_filtrados.groupby('mes')['vendas'].sum().reset_index()
fig = px.area(df_agrupado3,x='mes',y='vendas',title=f'evolucao mensal de {opcao}')
st.plotly_chart(fig,width='stretch')