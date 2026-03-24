import streamlit as st
import pandas as pd

# ── Configuração da página ─────────────────────────────────────────────────────
st.set_page_config(page_title="Mapa de Vendas", layout="wide")
st.title("🗺️ Mapas das Vendas por Região Filtrado")

# ── Carregar dados ─────────────────────────────────────────────────────────────
df = pd.read_csv(
    "dados/vendas_geolocalizacao.csv",
    encoding="utf-8"
)
dados_filtrados = df[df['Vendas']>0].copy()
st.dataframe(dados_filtrados.head())
# ── Tratamento de dados ─────────────────────────────────────────────────────────
df["Latitude"] = pd.to_numeric(df["Latitude"], errors="coerce")
df["Longitude"] = pd.to_numeric(df["Longitude"], errors="coerce")
df["Data"] = pd.to_datetime(df["Data"], errors="coerce")

# Remover vendas inválidas
df = df[df["Vendas"] > 0].copy()

# ── Sidebar Filtros ─────────────────────────────────────────────────────────────
st.sidebar.header("🎯 Filtros")

# Região
regioes = ["Todas"] + sorted(df["Região"].dropna().unique())
regiao_sel = st.sidebar.selectbox("Região", regioes)

# Categoria
categorias = ["Todas"] + sorted(df["Categoria"].dropna().unique())
categoria_sel = st.sidebar.selectbox("Categoria", categorias)

# Produto
produtos = ["Todos"] + sorted(df["Produto"].dropna().unique())
produto_sel = st.sidebar.selectbox("Produto", produtos)

# Vendedor
vendedores = ["Todos"] + sorted(df["Vendedor"].dropna().unique())
vendedor_sel = st.sidebar.selectbox("Vendedor", vendedores)

# Período
data_min = df["Data"].min().date()
data_max = df["Data"].max().date()

data_inicio, data_fim = st.sidebar.date_input(
   "Período",
    value=(data_min, data_max),
    min_value=data_min,
    max_value=data_max,)

# Faixa de vendas
venda_min = int(df["Vendas"].min())
venda_max = int(df["Vendas"].max())

faixa_vendas = st.sidebar.slider(
    "Faixa de Valor da Venda (R$)",
    min_value=venda_min,
    max_value=venda_max,
    value=(venda_min, venda_max),
    step=100,
)

# ── Aplicar filtros ─────────────────────────────────────────────────────────────
df_filtrado = df.copy()

if regiao_sel != "Todas":
    df_filtrado = df_filtrado[df_filtrado["Região"] == regiao_sel]

if categoria_sel != "Todas":
    df_filtrado = df_filtrado[df_filtrado["Categoria"] == categoria_sel]

if produto_sel != "Todos":
    df_filtrado = df_filtrado[df_filtrado["Produto"] == produto_sel]

if vendedor_sel != "Todos":
    df_filtrado = df_filtrado[df_filtrado["Vendedor"] == vendedor_sel]

df_filtrado = df_filtrado[
    (df_filtrado["Data"].dt.date >= data_inicio) &
    (df_filtrado["Data"].dt.date <= data_fim)
]

df_filtrado = df_filtrado[
    (df_filtrado["Vendas"] >= faixa_vendas[0]) &
    (df_filtrado["Vendas"] <= faixa_vendas[1])
]

# ── Métricas ────────────────────────────────────────────────────────────────────
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "📍 Pontos de Venda",
        df_filtrado.shape[0]
    )

with col2:
    st.metric(
        "🏙️ Cidades com Vendas",
        df_filtrado["Cidade"].nunique()
    )

with col3:
    st.metric(
        "💰 Total de Vendas",
        f"R$ {df_filtrado['Vendas'].sum():,.2f}"
    )

with col4:
    st.metric(
        "📈 Lucro Total",
        f"R$ {df_filtrado['Lucro'].sum():,.2f}"
    )

# ── Mapa ────────────────────────────────────────────────────────────────────────
dados_vendas = pd.read_csv(
    "dados/vendas_geolocalizacao.csv",
    usecols=["Latitude", "Longitude","Região", "Cidade", "Vendas", "Lucro"],
    sep=",",encoding="utf-8"
)
dados_vendas["Latitude"]=pd.to_numeric(dados_vendas["Latitude"],errors="coerce")
dados_vendas["Longitude"]=pd.to_numeric(dados_vendas["Longitude"],errors="coerce")
st.map(dados_vendas,latitude="Latitude",longitude="Longitude")

st.dataframe(dados_filtrados)