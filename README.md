## Mini-Projeto Avaliativo - Curso Análise de Dados com Python - SCTEC

# Análise Exploratória

### Exploração Inicial dos Dados

O arquivo `exploracao.py` realiza a leitura da base de dados e a inspeção inicial do DataFrame. Nesta etapa foram verificadas:

- Visualização das primeiras linhas da base;
- Quantidade de linhas e colunas;
- Nomes das colunas;
- Tipos de dados identificados;
- Quantidade de valores nulos por coluna;
- Estatísticas iniciais das colunas numéricas;
- Valores únicos de colunas categóricas.

### Principais descobertas

Durante a importação foi identificado que o arquivo CSV utiliza o caractere `;` como separador de colunas. Inicialmente o pandas interpretou todo o conteúdo como uma única coluna, sendo necessário informar o delimitador corretamente na leitura do arquivo.

### Inconsistências identificadas

#### Colunas Float totalmente vazias

- `Unnamed: 10`
- `Unnamed: 11`
- `Unnamed: 12`
- `Unnamed: 13`

#### Colunas String

- `CL_GENERO` sem inconsistências aparentes;
- `CL_SEG` sem inconsistências aparentes;
- `PR_CAT` possui registros com valor `#N/D`.

#### Colunas Integer

As colunas abaixo não apresentaram inconsistências aparentes:

- `CO_ID`
- `CL_ID`
- `CL_EC`
- `CL_FHL`
- `PR_ID`

#### Coluna Date

A coluna `DATA` está sendo interpretada como `object`, sendo necessária a conversão para o tipo `datetime`.
