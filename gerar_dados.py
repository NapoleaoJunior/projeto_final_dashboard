import pandas as pd
import numpy as np

np.random.seed(42)
n = 2000
datas = pd.date_range('2023-01-01','2025-12-31', freq='D')
# Gerar dados de vendas
dados = pd.DataFrame({'data': np.random.choice(datas,n),
                      'produto': np.random.choice(['headset', 'teclado', 'mouse','notebook','ssd','monitor'], n),
                      'categoria':np.random.choice(['eletrônicos', 'periféricos'], n),
                      'região': np.random.choice(['norte', 'sul', 'leste', 'oeste'], n),
                      'vendedor': np.random.choice(['Alice', 'Bob', 'Charlie', 'David','carlos','diana','paulo'], n),
                      'vendas': np.random.randint(150, 12000, n),
                      'quantidade': np.random.randint(1, 30, n),
                      'custo': np.random.uniform(50, 8000, n)})