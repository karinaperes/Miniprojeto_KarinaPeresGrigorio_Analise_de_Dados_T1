## Mini-Projeto Avaliativo - Curso Análise de Dados com Python - SCTEC

O processo de ETL (Extract, Transform and Load) é fundamental para garantir que os dados utilizados em análises estejam organizados, padronizados e confiáveis.

Durante o projeto foi possível identificar inconsistências como colunas vazias, categorias inválidas, registros duplicados e diferenças entre identificadores de produtos. Essas inconsistências demonstram a importância da qualidade dos dados para evitar análises incorretas e garantir resultados mais confiáveis.

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

A análise exploratória permitiu identificar problemas relevantes de qualidade dos dados na base, como colunas completamente vazias, valores inválidos em categorias, registros duplicados e inconsistências entre identificadores de produtos. Também foi necessário ajustar o processo de leitura do arquivo CSV e realizar conversões manuais de tipos de dados para garantir o funcionamento correto das análises estatísticas e das etapas de limpeza.
Também foi identificado que os registros com valor #N/D na coluna PR_CAT estavam associados aos mesmos registros com valor #N/D na coluna PR_NOME.

Conforme solicitado no documento da atividade, os valores inválidos da coluna PR_CAT foram substituídos por SEM CATEGORIA.

Já na coluna PR_NOME, os valores #N/D foram convertidos para pd.NA, pois representam ausência de identificação do produto e não havia regra definida para substituição desses registros.

### Alteração na Leitura do CSV

Inicialmente a leitura do arquivo foi realizada utilizando pandas.read_csv(), devido à praticidade da biblioteca para importação de dados tabulares.

Posteriormente, ao revisar os requisitos do documento do projeto, foi identificado que a avaliação solicitava a utilização do módulo nativo csv.DictReader para a etapa de extração dos dados.

Durante essa alteração surgiu um problema importante: todas as colunas passaram a ser importadas como texto (string/object), já que o csv.DictReader não realiza inferência automática de tipos como o pandas.

Isso causou erros nas análises estatísticas, especialmente na execução do método describe(), além de falhas em operações matemáticas e cálculos estatísticos, pois colunas numéricas estavam sendo interpretadas como texto.

Para resolver o problema, foi necessário converter manualmente as colunas numéricas utilizando pd.to_numeric().

### Inconsistências identificadas

#### Colunas totalmente vazias

Na leitura inicial utilizando `pandas.read_csv()`, foram identificadas múltiplas colunas vazias nomeadas automaticamente como `Unnamed`, com tipo `float64`, devido à inferência automática de tipos realizada pelo pandas.

Após a alteração para `csv.DictReader`, essas colunas passaram a ser interpretadas como uma única coluna sem nome (`''`) e com tipo `object`, pois o módulo `csv` realiza uma leitura mais literal do arquivo, sem inferência automática de estrutura e tipos de dados.

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

Conforme resultado da análise exploratória, foram aplicadas as seguintes correções:

- Limpeza de texto remoção de espaços extras, acentos e conversão para maiúsculo
- Remoção das colunas vazias
- Substituição de valores nulos `#N/D` para `SEM CATEGORIA`, conforme requerido no documento do projeto
- Limpeza e conversão da coluna `DATA` de `object` para `datetime`

## Estatística Descritiva

O arquivo estatistica.py realiza a análise estatística da coluna CL_FHL (quantidade de filhos dos clientes).

#### Métricas calculadas

- Média;
- Mediana;
- Moda;
- Valor mínimo;
- Valor máximo;
- Desvio padrão;
- Contagem de registros;
- Quartis.

#### Resultados encontrados

- Média de filhos: 1.14
- Mediana: 0
- Moda: 0
- Máximo: 4
- Mínimo: 0

Os resultados indicam que a maior parte dos clientes não possui filhos.

## Análise de Duplicatas e Consistência

Durante a análise exploratória foram identificadas:

96.553 linhas completamente duplicadas considerando todas as colunas;
176.327 registros duplicados considerando apenas CO_ID, PR_NOME e DATA.

A remoção automática dessas duplicatas não foi aplicada inicialmente, pois a base não possui uma coluna de quantidade de itens comprados, indicando que registros repetidos podem representar compras legítimas do mesmo produto na mesma data.

Também foi realizada uma análise de consistência entre identificadores de produtos.

## Relação entre PR_ID e PR_NOME

Foi identificado que:

Cada PR_ID está associado a apenas um PR_NOME;
Porém, diversos PR_NOME possuem mais de um PR_ID.

Foram encontrados 109 produtos com múltiplos identificadores, como:

ARROZ → [227, 8]
ATUM → [225, 10]
VASSOURA → [114, 120]

Esse comportamento pode indicar:

Duplicidade de cadastro;
Variações do mesmo produto cadastradas com IDs diferentes;
Inconsistências na modelagem da base.

## Relação entre PR_CAT, PR_NOME e PR_ID

A análise por categoria mostrou divergência entre quantidade de nomes de produtos e quantidade de IDs:

| Categoria | PR_NOME únicos | PR_ID únicos |
| --------- | -------------- | ------------ |
| ALIMENTOS | 61             | 120          |
| HIGIENE   | 22             | 43           |
| LIMPEZA   | 21             | 40           |
| BEBIDAS   | 6              | 12           |

Os resultados indicam possível inconsistência entre identificadores de produtos. A unificação dos PR_ID não foi aplicada por falta de informações que permitam identificar qual código deve ser considerado correto.
