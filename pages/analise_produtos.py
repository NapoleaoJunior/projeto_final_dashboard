import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from pathlib import Path

st.markdown(
    """
    <style>
        .stApp { background-color: #e6f7ff; } /* fundo azul claro */
    </style>
    """,
    unsafe_allow_html=True
)

st.title("💰 Análise detalhada dos produtos")

produtos   = sorted(["headset", "teclado", "mouse", "notebook", "ssd", "monitor"])
categorias = sorted(["eletrônicos", "periféricos"])
regioes    = sorted(["norte", "sul", "leste", "oeste"])
vendedores = sorted(["Alice", "Bob", "Charlie", "David", "Carlos", "Diana", "Paulo", "Elena"])

options = st.selectbox(
    "selecione um produto",
    options=produtos,
    index=0
)
df_valor_venda = pd.read_csv("dados/dados_vendas.csv")
df_filtrado = df_valor_venda[df_valor_venda['produto']==options]
st.subheader(f"Vendas do produto: {options}")
st.line_chart(df_filtrado["vendas"])

@st.cache_data
def carregar_dados_demo(n: int = 1000,
                        data_inicio: str = "2024-01-01",
                        data_fim: str = "2024-12-31",
                        seed: int = 42) -> pd.DataFrame:
    np.random.seed(seed)
    datas = pd.date_range(start=data_inicio, end=data_fim, freq="D")

    df = pd.DataFrame({
        "data":       np.random.choice(datas, n),
        "produto":    np.random.choice(produtos, n),
        "categoria":  np.random.choice(categorias, n),
        "regiao":     np.random.choice(regioes, n),
        "vendedor":   np.random.choice(vendedores, n),
        "valor_venda": np.random.randint(150, 12000, n).astype(float),
        "quantidade": np.random.randint(1, 30, n).astype(int),
        "custo_unit": np.random.uniform(80, 8000, n)
    })

    # Receita = total da venda por linha (se preferir, mude a lógica para preço*quantidade)
    df["receita"]    = df["valor_venda"].round(2)
    df["custo_unit"] = df["custo_unit"].round(2)
    df["data"]       = pd.to_datetime(df["data"])
    return df

dados_produto = carregar_dados_demo()

def to_number_br(serie: pd.Series) -> pd.Series:
    if pd.api.types.is_numeric_dtype(serie):
        return serie
    serie = serie.astype(str).str.strip()
    serie = serie.str.replace('.', '', regex=False).str.replace(',', '.', regex=False)
    return pd.to_numeric(serie, errors="coerce")

def ensure_datetime(s: pd.Series) -> pd.Series:
    if pd.api.types.is_datetime64_any_dtype(s):
        return s
    return pd.to_datetime(s, errors="coerce", dayfirst=True, utc=False)

required = {"produto", "vendedor", "data", "receita"}
faltantes = required - set(dados_produto.columns)
if faltantes:
    st.error(f"Colunas obrigatórias ausentes: {sorted(faltantes)}")
    st.stop()

dados_produto = dados_produto.copy()
dados_produto["data"] = ensure_datetime(dados_produto["data"])
dados_produto["receita"] = to_number_br(dados_produto["receita"])
dados_produto = dados_produto.dropna(subset=["data"])
dados_produto["receita"] = dados_produto["receita"].fillna(0.0)

st.sidebar.header("Filtros de produtos")

opts_prod = sorted(dados_produto["produto"].dropna().unique())
opts_vend = sorted(dados_produto["vendedor"].dropna().unique())

prod_sel = st.sidebar.multiselect("Selecione os produtos", options=opts_prod, default=opts_prod)
vend_sel = st.sidebar.multiselect("Selecione os vendedores", options=opts_vend, default=opts_vend)

dmin = dados_produto["data"].min().date()
dmax = dados_produto["data"].max().date()
data_sel = st.sidebar.date_input("Selecione a data", value=dmin, min_value=dmin, max_value=dmax)

inicio = pd.to_datetime(data_sel)
fim = inicio + pd.Timedelta(days=1) - pd.Timedelta(seconds=1)

dados_filtrados = dados_produto[
    (dados_produto["produto"].isin(prod_sel)) &
    (dados_produto["vendedor"].isin(vend_sel)) &
    (dados_produto["data"] >= inicio) &
    (dados_produto["data"] <= fim)
].copy()

col1, col2, col3 = st.columns(3)

valor_total = float(dados_filtrados["receita"].sum())
fmt_us = f"{valor_total:,.0f}"               # 1,234,567
fmt_br = fmt_us.replace(",", "X").replace(".", ",").replace("X", ".")
col1.metric("Receita filtrada", f"R$ {fmt_br}")

itens = int(dados_filtrados["produto"].count())
col2.metric("Itens filtrados", f"{itens:,}".replace(",", "."))

vendedores_uniq = int(dados_filtrados["vendedor"].nunique())
col3.metric("Vendedores (únicos)", f"{vendedores_uniq:,}".replace(",", "."))

if not dados_filtrados.empty:
    top = (dados_filtrados.groupby("produto", as_index=False)["receita"]
           .sum()
           .sort_values("receita", ascending=False)
           .head(10))
    fig = px.bar(top, x="produto", y="receita",
                 title="Top 10 produtos por receita (filtro aplicado)",
                 text_auto=True)
    fig.update_layout(yaxis_tickprefix="R$ ")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("Nenhum dado encontrado para os filtros selecionados.")

