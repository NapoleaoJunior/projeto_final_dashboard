# Dashboard de Análise de Vendas Multiplaforma

## 📊 Descrição do Projeto

Dashboard interativo desenvolvido para análise e visualização de dados de vendas. O projeto permite visualizar métricas de desempenho, análises de produtos e visualizações geográficas das vendas em tempo real.

## 🎯 Objetivo

Fornecer uma ferramenta completa para análise de vendas com interface amigável, permitindo:
- Visualizar indicadores de desempenho (KPIs)
- Analisar vendas por produtos
- Explorar dados geográficos de vendas
- Gerar insights sobre comportamento de vendas

## 🛠️ Tecnologias Utilizadas

- **Python 3.x** - Linguagem de programação principal
- **Streamlit** - Framework para criação de aplicações web interativas
- **Pandas** - Manipulação e análise de dados
- **NumPy** - Computação numérica
- **Plotly** - Visualizações gráficas interativas
- **PyDeck** - Visualizações de mapas geográficos
- **Pillow** - Processamento de imagens

## 📁 Estrutura do Projeto

```
projeto_final_dashboard/
├── app.py                          # Arquivo principal da aplicação
├── gerar_dados.py                  # Script para geração de dados
├── requirements.txt                # Dependências do projeto
├── README.md                       # Este arquivo
├── dados/
│   ├── dados_vendas.csv           # Dados de vendas
│   └── vendas_geolocalizacao.csv  # Dados com geolocalização
├── img/                            # Imagens do projeto
└── pages/
    ├── visao_geral.py             # Página inicial com visão geral
    ├── analise_vendas.py          # Análise detalhada de vendas
    ├── analise_produtos.py        # Análise de produtos
    ├── analise_produtos_professor.py # Análise de produtos (versão professor)
    ├── mapas_vendas.py            # Mapa de vendas por região
    ├── mapas_vendas2.py           # Mapa filtrado de vendas por região
    └── sobre.py                   # Página sobre o projeto
```

## 📑 Funcionalidades Principais

- **Visão Geral** - Dashboard com indicadores principais e métricas gerais
- **Análise de Vendas** - Visualizações e filtros para análise detalhada de vendas
- **Análise de Produtos** - Desempenho de produtos com diversos filtros
- **Mapas de Vendas** - Visualizações geográficas das vendas por região
- **Interface Responsiva** - Design adaptável para diferentes plataformas

## 🚀 Como Executar

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes)

### Instalação

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd projeto_final_dashboard
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
```

3. Ative o ambiente virtual:

**No Windows:**
```bash
venv\Scripts\activate
```

**No Linux/Mac:**
```bash
source venv/bin/activate
```

4. Instale as dependências:
```bash
pip install -r requirements.txt
```

### Executar a Aplicação

```bash
streamlit run app.py
```

A aplicação será aberta em `http://localhost:8501`

## 📋 Dependências Principais

- streamlit==1.55.0
- pandas==2.3.3
- plotly==6.6.0
- pydeck==0.9.1
- numpy==2.4.3
- pillow==12.1.1

Para uma lista completa, consulte o arquivo `requirements.txt`.

## 👨‍💻 Autor

Projeto Final - SENAC DF

## 📝 Notas

- Os dados utilizados estão armazenados em arquivos CSV na pasta `dados/`
- O script `gerar_dados.py` pode ser utilizado para gerar novos dados de teste
- A paleta de cores utiliza um tema azul claro para melhor legibilidade
