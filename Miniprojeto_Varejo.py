import csv
import pandas as pd
from datetime import datetime

# ==========================================
# SPRINT 1 & 3: IMPORTAÇÃO E LEITURA 
# ==========================================
print("Iniciando a Análise Exploratória da Base Varejo...")

caminho_arquivo = 'Base Varejo.csv'
dados_brutos = []

# Critério 3: Leitura estruturada e nativa utilizando csv.DictReader com o delimitador correto
with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo:
    leitor_csv = csv.DictReader(arquivo, delimiter=';')
    for linha in leitor_csv:
        # Limpeza inicial: ignorando colunas vazias criadas por delimitadores extras (;;;;) no CSV
        linha_limpa = {k: v for k, v in linha.items() if k and k.strip() != ''}
        dados_brutos.append(linha_limpa)

df = pd.DataFrame(dados_brutos)

# ==========================================
# SPRINT 2 & 3: TRATAMENTO DE NULOS E DATAS 
# ==========================================

# 1. Regra de Negócio: if/else para Categorias Vazias (PR_CAT)
def preencher_categoria(categoria):
    # Tratando nulos, espaços em branco e a marcação de erro '#N/D' encontrada na base real
    if pd.isna(categoria) or str(categoria).strip() == '' or categoria == '#N/D':
        return "Sem Categoria"
    else:
        return categoria

df['PR_CAT'] = df['PR_CAT'].apply(preencher_categoria)

# 2. Tratamento de Nulos das "Dimensões Físicas" (Critério 4)
# Justificativa: Ao inspecionar a base, constatou-se que não há uma dimensão física explícita.
# No entanto, os erros de formatação geraram colunas fantasmas (Unnamed) 100% nulas.
# O tratamento aplicado foi a exclusão dessas colunas sem dados para garantir a integridade.
df = df.dropna(axis=1, how='all')

# 3. Conversão de Data usando o módulo datetime nativo (Critério 5)
def converter_data(data_str):
    try:
        # Formato identificado na base: DD/MM/YYYY
        return datetime.strptime(data_str, '%d/%m/%Y').date()
    except Exception:
        return pd.NaT

df['DATA'] = df['DATA'].apply(converter_data)

# 4. Validar regra do identificador de número de compra (CO_ID)
def validar_id_compra(co_id):
    if pd.isna(co_id) or not str(co_id).isdigit():
        return "ID_Invalido"
    return str(co_id)

df['CO_ID'] = df['CO_ID'].apply(validar_id_compra)
# Mantendo apenas transações com IDs válidos
df = df[df['CO_ID'] != "ID_Invalido"]

# ==========================================
# SPRINT 4: ESTATÍSTICA DESCRITIVA
# ==========================================
print("\n--- Estatísticas Descritivas: Número de Filhos (CL_FHL) ---")

# Critério 7: Conversão da coluna CL_FHL para realizar os cálculos matemáticos
df['CL_FHL'] = pd.to_numeric(df['CL_FHL'], errors='coerce')

estatisticas_filhos = {
    'Média': df['CL_FHL'].mean(),
    'Mediana': df['CL_FHL'].median(),
    'Desvio Padrão': df['CL_FHL'].std(),
    'Moda': df['CL_FHL'].mode()[0],
    'Máximo': df['CL_FHL'].max(),
    'Mínimo': df['CL_FHL'].min(),
    'Contagem': df['CL_FHL'].count(),
    'Quartis': df['CL_FHL'].quantile([0.25, 0.5, 0.75]).to_dict()
}

for chave, valor in estatisticas_filhos.items():
    # Arredondando floats para 2 casas decimais para manter o terminal limpo
    print(f"{chave}: {round(valor, 2) if isinstance(valor, float) else valor}")

# ==========================================
# SPRINT 4: PADRÕES DE AGRUPAMENTO 
# ==========================================
print("\n--- Padrões de Agrupamento ---")

# Critério 6: Padrões com pelo menos duas combinações
# Combinação 1: Volume de itens adquiridos por Gênero (CL_GENERO)
agrupamento_genero = df.groupby('CL_GENERO')['PR_ID'].count()
print("Volume de Produtos por Gênero:\n", agrupamento_genero)

# Combinação 2: Cruzamento de Categoria do Produto (PR_CAT) e Gênero do Cliente via pivot_table
agrupamento_cat_gen = df.pivot_table(index='PR_CAT', columns='CL_GENERO', values='CO_ID', aggfunc='count')
print("\nVolume de Compras por Categoria e Gênero:\n", agrupamento_cat_gen)