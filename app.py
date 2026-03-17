import streamlit as st

# mudar cor de fundo
st.markdown("""
    <style>
        .stApp {
            background-color: #e6f7ff; /* cor azul clara */
        }
    </style>
""", unsafe_allow_html=True)

st.set_page_config(
    page_title="dashboard de vendas",
    page_icon=":bar_chart:",
    layout="wide"
)
#definido paginas
visao_geral = st.Page("./pages/visao_geral.py",title="visao geral",
                      icon="🏠",default=True)
analise_vendas = st.Page('./pages/analise_vendas.py',title='analise de vendas',icon='📦')
analise_produtos = st.Page('./pages/analise_produtos.py',title='analise por produtos',icon='📦')
#sobre = st.Page('./sobre.py',title='sobre',icon=':information_sourse:')
#configurando navegacao entre paginas
pg = st.navigation([visao_geral,analise_vendas,analise_produtos])
pg.run()