# Pipeline de ETL Local

Este repositório contém um pipeline de ETL (Extração, Transformação e Carga) para processar dados de produção de alimentos e armazená-los em um banco de dados SQLite.

## Estrutura do Repositório
project_ETL/
    pipeline_local/
        producao_alimentos.csv  # Arquivo CSV com os dados de produção de alimentos
        pipeline.py             # Script principal do pipeline ETL
        eng_eba.db               # Banco de dados SQLite gerado pelo scri

## Tecnologias Utilizadas

- Python
- SQLite
- CSV

## Funcionalidades

1. **Extração**: O script abre e lê um arquivo CSV contendo informações sobre produção de alimentos.
2. **Transformação**: Calcula a margem de lucro com base nos dados extraídos.
3. **Carga**: Insere os dados processados em um banco de dados SQLite.
4. **Validação**: Exibe os dados armazenados para conferência.

## Requisitos

Antes de executar o pipeline, certifique-se de ter instalado:

- Python 3.12.6

## Como Executar

1. Repositório:
   git clone https://github.com/ludovina-magalhaes/pipeline_local.git

2. Acesse o diretório do projeto:
   cd pipeline_local/project_ETL/pipeline_local

3. Execute o script:
   python pipeline.py
   

## Script Principal

O script **pipeline.py** executa os seguintes passos:

- Cria um banco de dados SQLite e uma tabela "producao".
- Lê os dados do arquivo CSV "producao_alimentos.csv".
- Insere apenas os registros com quantidade superior a 10.
- Calcula a margem de lucro e insere os dados na tabela "producao".
- Exibe os dados armazenados no banco.

## Exemplo de Saída
Pipeline concluído com sucesso



## Autor

Ludovina Magalhães

