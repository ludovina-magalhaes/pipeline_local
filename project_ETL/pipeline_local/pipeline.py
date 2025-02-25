import csv
import sqlite3

# Criar uma conexão com o banco de dados
conn = sqlite3.connect('eng_eba.db')
cursor = conn.cursor()

# Criar a tabela apenas se ainda não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS producao (
        produto TEXT,
        quantidade REAL,
        preco_medio REAL,
        receita_total REAL,
        custo_kg REAL,
        margem_lucro REAL
    )
''')

conn.commit()
conn.close()

# Abrir o arquivo CSV com os dados de produção de alimentos
with open('producao_alimentos.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # Pular a primeira linha do CSV

    # Criar uma nova conexão
    conn = sqlite3.connect('eng_eba.db')
    cursor = conn.cursor()

    # Inserir os dados do CSV no banco de dados
    for row in reader:
        if float(row[1]) > 10:  # Comparação corrigida
            
            # Calcular a margem de lucro
            receita_total = float(row[3])
            custo_total = float(row[1]) * float(row[4])
            margem_lucro = (receita_total - custo_total) / receita_total if receita_total != 0 else 0

            # Inserir os dados
            cursor.execute('''
                INSERT INTO producao (produto, quantidade, preco_medio, receita_total, custo_kg, margem_lucro)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (row[0], row[1], row[2], row[3], row[4], margem_lucro))

    conn.commit()
    conn.close()

print('Pipeline concluído com sucesso')

# Verificando se os dados estão na base de dados
conn = sqlite3.connect('eng_eba.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM producao")
resultados = cursor.fetchall()

for linha in resultados:
    print(linha)

conn.close()

