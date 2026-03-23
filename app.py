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
analise_produtos_professor = st.Page('./pages/analise_produtos_professor.py',
                                     title='analise por produtos - professor',icon='📦')
mapas_vendas = st.Page('./pages/mapas_vendas.py',
                                     title='Mapas de vendas por Regiao',icon='🗺️')
sobre = st.Page('./pages/sobre.py',title='sobre',icon='ℹ️')
#sobre = st.Page('./sobre.py',title='sobre',icon=':information_sourse:')
#configurando navegacao entre paginas
pg = st.navigation([visao_geral,analise_vendas,
                    analise_produtos,analise_produtos_professor,mapas_vendas,sobre])
pg.run()