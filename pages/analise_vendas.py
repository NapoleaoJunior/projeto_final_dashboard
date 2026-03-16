import streamlit as st
import pandas as pd
import plotly.express as px

# mudar cor de fundo
st.markdown("""
    <style>
        .stApp {
            background-color: #e6f7ff; /* cor azul clara */
        }
    </style>
""", unsafe_allow_html=True)

def carregar_dados():
    df = pd.read_csv('dados/dados_vendas.csv')
    df['data']=pd.to_datetime(df['data'])
    return df
dado_vendas = carregar_dados()
st.title(':moneybag: analise detalhada de vendas')
#filtros
st.sidebar.header("filtros de vendas")

regioes = st.sidebar.multiselect("selecione as regiões",
                                  options=dado_vendas['região'].unique(),
                                  default=dado_vendas['região'].unique())

categorias = st.sidebar.multiselect("selecione as categorias",
                                     options=dado_vendas['categoria'].unique(),
                                     default=dado_vendas['categoria'].unique())

data_mim = dado_vendas['data'].min().date()
data_max = dado_vendas['data'].max().date()
# filtro por uma única data (FORMA MAIS SEGURA)
data_selecionada = st.sidebar.date_input(
    "Selecione a data",
    value=data_mim,
    min_value=data_mim,
    max_value=data_max
)

# Converte para datetime (início do dia)
inicio = pd.to_datetime(data_selecionada)

# Final do mesmo dia (23:59:59)
fim = inicio + pd.Timedelta(days=1) - pd.Timedelta(seconds=1)

# Aplicar filtros
dados_filtrados = dado_vendas[
    (dado_vendas['região'].isin(regioes)) &
    (dado_vendas['categoria'].isin(categorias)) &
    (dado_vendas['data'] >= inicio) &
    (dado_vendas['data'] <= fim)
]
col1,col2,col3 = st.columns(3)
col1.metric("receita filtrada",f"R$ {dados_filtrados['vendas'].sum():,.0f}")
col2.metric("lucro filtrado",f"R$ {dados_filtrados['lucro'].sum():,.0f}")
#calcular margem de lucro
margem_media = 'N/A'
if dados_filtrados['vendas'].sum()>0:
    margem_media = (dados_filtrados['lucro'].sum() / dados_filtrados['vendas'].sum()*100)
    col3.metric("margem média",f"{margem_media}%")
#vendas por vendedor
#a análise de vendas por vendedor é crucial para 
# identificar os melhores desempenhos e áreas de melhoria.
#e calcular receita, lucro, transações e ticket médio por vendedor
# os resultados são arredondados para 2 casas decimais e ordenados 
# por receita em ordem decrescente para destacar os vendedores mais lucrativos.
st.subheader(":bust_in_silhouette: performance por vendedor")
vendas_vendedor = dados_filtrados.groupby('vendedor').agg(
    receita =('vendas','sum'),
    lucro =('lucro','sum'),
    transacoes =('vendas','count'),
    ticket_medio =('vendas','mean')
).round(2).sort_values(by='receita', ascending=False)
v_col1,v_col2 = st.columns(2)
with v_col1:
    st.dataframe(vendas_vendedor,width='stretch')
with v_col2:
    fig = px.bar(
        vendas_vendedor.reset_index(),
        x='vendedor',
        y='receita',
        title='receita e lucro por vendedor',
        color='lucro',
        color_continuous_scale='sunset',
    )
    st.plotly_chart(fig,width='stretch')
#analise temporal de vendas
st.subheader(":calendar: analise temporal de vendas")
dados_filtrados['mes']=dados_filtrados['data'].dt.to_period('M').astype(str)
mensal = dados_filtrados.groupby('mes').agg(
    receita =('vendas','sum'),
    lucro=('lucro','sum')
).reset_index()
fig = px.bar(
    mensal,
    x='mes',
    y=['receita','lucro'],
    barmode='group',
    title='receita X lucro mensal')
fig.update_layout(xaxis_title=-45)
st.plotly_chart(fig,width='stretch')
