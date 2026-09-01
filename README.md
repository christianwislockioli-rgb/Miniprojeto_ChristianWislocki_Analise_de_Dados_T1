# Análise Exploratória de Dados - Varejo

Projeto de avaliação do Módulo 1 (Semana 07) focado na qualidade e limpeza de dados utilizando Python.

## Como Executar
1. Clone este repositório.
2. Abra a pasta no VS Code.
3. Certifique-se de ter o Pandas instalado (`pip install pandas`).
4. Execute no terminal: `python Miniprojeto_Varejo.py`.

## Reflexão Teórica: ETL e Qualidade de Dados
Um processo de Extração, Transformação e Carga (ETL) rigoroso é o alicerce de qualquer análise confiável. Quando bases de dados apresentam valores nulos, formatos inconsistentes ou erros estruturais de exportação (como os delimitadores extras encontrados neste projeto), os indicadores gerados tornam-se enviesados. Tanto na esfera corporativa quanto na gestão pública, tomar decisões com base em dados "sujos" resulta em alocação ineficiente de recursos e formulação de estratégias equivocadas. A etapa de limpeza e tratamento prévio é o que garante que os relatórios e painéis reflitam a verdadeira realidade operacional, permitindo uma tomada de decisão analítica, segura e baseada em evidências.

## Principais Insights da Análise
1. **O perfil predominante:** Mulheres representam a maioria do volume total de itens comprados, respondendo por 52,1% (432.576) das transações. Elas superam o público masculino no volume de compras em absolutamente todas as categorias de produtos oferecidas.
2. **Impacto familiar segmentado:** A maioria da base de clientes não possui filhos, o que é comprovado pela Mediana e Moda iguais a 0 (além do 1º e 2º quartis estarem zerados). Contudo, a média (1,15) é puxada para cima por um nicho específico de famílias, visto que 25% da base superior (3º quartil) possui 2 filhos, chegando ao máximo de 4.
3. **O carro-chefe de vendas:** O setor de "Alimentos" é o principal motor de giro do varejo, somando mais de 434 mil registros de itens adquiridos (mais da metade de todo o volume da base), seguido de longe pelos setores de Higiene e Limpeza.
4. **Tratamento de categorias vazias:** Foi identificado que exatamente 3.650 registros apresentavam falhas ou ausência no cadastro da categoria do produto. Eles foram classificados como "Sem Categoria" para que o registro da compra não fosse descartado, preservando assim a volumetria da base.
5. **Problemas estruturais remanescentes:** A base original apresenta falhas de exportação (delimitadores sobrando no CSV), o que gera colunas fantasmas e vazias ao longo de seus 830 mil registros. Foi necessária a limpeza dessas anomalias para não comprometer a leitura dos dados, destacando um problema na origem do sistema que gerou o arquivo.