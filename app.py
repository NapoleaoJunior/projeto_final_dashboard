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
#analise_vendas = st.Page('./pages/analise_vendas.py',title='produtos',icon=':package:')
#analise_produtos = st.page('./pages/analise_produtos.py',title='produtos',icon=':package:')
#sobre = st.Page('./sobre.py',title='sobre',icon=':information_sourse:')
#configurando navegacao entre paginas
pg = st.navigation([visao_geral])
pg.run()
