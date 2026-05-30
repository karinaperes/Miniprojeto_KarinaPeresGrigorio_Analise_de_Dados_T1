# Mini-Projeto Avaliativo - Análise de Dados com Python

## Objetivo

Realizar uma Análise Exploratória de Dados (AED) da base Varejo, aplicando conceitos de ETL, limpeza de dados, estatística descritiva e análise de padrões de agrupamento.

---

## Tecnologias Utilizadas

- Python 3
- Pandas
- CSV (csv.DictReader)

---

## Estrutura do Projeto

```text
Miniprojeto_KarinaPeresGrigorio_Analise_de_Dados_T1/

├── dados/
│   ├── Base_Varejo.csv
│   └── Base_Varejo_Limpa.csv
|
├── src/
│   ├── main.py
│   ├── exploracao.py
│   ├── limpeza.py
│   └── estatistica.py
|
├── README.md
├── README_KarinaPeresGrigorio_Analise_de_Dados_T1.md
├── requirements.txt
└── .gitignore
```

## Como Executar

1. Clonar o repositório `git clone URL_DO_REPOSITORIO`
2. Acessar a pasta do projeto `cd Miniprojeto_KarinaPeresGrigorio_Analise_de_Dados_T1`
3. Criar ambiente virtual `python -m venv .venv`
4. Ativar ambiente virtual

- Git Bash:
```bash
source .venv/Scripts/activate
```
- Prompt de Comando:
```
.venv\Scripts\activate
```
5. Instalar dependências `pip install -r requirements.txt`
6. Executar o projeto

   `cd src`

   `python main.py`

### Saídas Geradas

Durante a execução são exibidos:

- Informações gerais da base;
- Valores nulos;
- Valores inválidos;
- Duplicatas;
- Correspondência entre produtos e identificadores;
- Estatísticas da coluna de filhos;
- Agrupamentos por gênero e segmento.

Também é gerado automaticamente o arquivo:

`dados/Base_Varejo_Limpa.csv`

contendo a base após as etapas de limpeza.
