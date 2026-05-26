## Mini-Projeto Avaliativo - Curso Análise de Dados com Python - SCTEC

# Análise Exploratória

### Exploração Inicial dos Dados

O arquivo exploracao.py realiza a leitura da base de dados e a inspeção inicial do DataFrame. Nesta etapa foram verificadas as informações básicas da estrutura dos dados, incluindo:

- Visualização das primeiras linhas da base;
- Quantidade de linhas e colunas;
- Nomes das colunas;
- Tipos de dados identificados;
- Quantidade de valores nulos por coluna.

### Principais descobertas

Durante a importação foi identificado que o arquivo CSV utiliza o caractere ; como separador de colunas. Inicialmente o pandas interpretou todo o conteúdo como uma única coluna, sendo necessário informar o delimitador na leitura do arquivo.

Também foram identificadas quatro colunas nomeadas automaticamente como:

- Unnamed: 10
- Unnamed: 11
- Unnamed: 12
- Unnamed: 13

Essas colunas serão investigadas nas próximas etapas para verificar se contêm informações relevantes ou se representam inconsistências na estrutura do arquivo.

Além disso, foi observado que a coluna DATA está sendo interpretada como object, será necessário a conversão para o tipo datetime durante o processo de limpeza e preparação dos dados.
