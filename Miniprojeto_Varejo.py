import csv
import pandas as pd
from datetime import datetime

# ==========================================
# SPRINT 1 & 3: IMPORTAÇÃO E LEITURA (Critério 3)
# ==========================================
print("Iniciando a Análise Exploratória da Base Varejo...")

# Lendo de forma estruturada e nativa conforme exigido na rubrica
caminho_arquivo = 'Base Varejo.csv'
dados_brutos = []

with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo:
    leitor_csv = csv.DictReader(arquivo)
    for linha in leitor_csv:
        dados_brutos.append(linha)

# Convertendo para DataFrame para facilitar o restante da AED
df = pd.DataFrame(dados_brutos)

# ==========================================
# SPRINT 2 & 3: TRATAMENTO DE NULOS E DATAS (Critérios 4 e 5)
# ==========================================

# 1. Regra de Negócio: if/else para Categorias Vazias
def preencher_categoria(categoria):
    if pd.isna(categoria) or categoria.strip() == '':
        return "Sem Categoria"
    else:
        return categoria

df['Categoria'] = df['Categoria'].apply(preencher_categoria)

# 2. Tratamento de dimensões físicas (Exemplo: preencher com 0 ou a média, e justificar)
# JUSTIFICATIVA (coloque no print e no README): Optou-se por preencher valores nulos 
# de dimensões físicas com a mediana/0 para não distorcer a análise de volume.
# df['Dimensao'] = df['Dimensao'].fillna(0) # Adapte para a coluna real da base

# 3. Conversão de Data usando o módulo datetime exigido
def converter_data(data_str):
    try:
        # Ajuste o formato '%Y-%m-%d' conforme o padrão que vier no CSV
        return datetime.strptime(data_str, '%Y-%m-%d').date()
    except:
        return pd.NaT

df['Data_Compra'] = df['Data_Compra'].apply(converter_data)

