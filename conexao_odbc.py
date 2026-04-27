import psycopg2

# Conexão com o banco
conn = psycopg2.connect(
    host="localhost",
    database="atividade_db",
    user="lelebiglove",
    password="senha123"
)

cur = conn.cursor()

# 1. Inserir uma atividade em algum projeto
print("=== INSERINDO ATIVIDADE ===")
cur.execute("""
    INSERT INTO atividade (descricao, projeto, data_inicio, data_fim)
    VALUES ('Nova Atividade - Teste ODBC', 1, '2024-01-01', '2024-06-30')
    RETURNING codigo, descricao;
""")
nova_atividade = cur.fetchone()
print(f"Atividade inserida: Código={nova_atividade[0]}, Descrição={nova_atividade[1]}")

# 2. Atualizar o líder de algum projeto
print("\n=== ATUALIZANDO LÍDER DO PROJETO ===")
cur.execute("""
    UPDATE projeto 
    SET responsavel = 1 
    WHERE codigo = 3
    RETURNING codigo, nome, responsavel;
""")
projeto_atualizado = cur.fetchone()
print(f"Projeto atualizado: Código={projeto_atualizado[0]}, Nome={projeto_atualizado[1]}, Novo responsável={projeto_atualizado[2]}")

# 3. Listar todos os projetos e suas atividades
print("\n=== PROJETOS E ATIVIDADES ===")
cur.execute("""
    SELECT p.codigo, p.nome, a.codigo, a.descricao
    FROM projeto p
    LEFT JOIN atividade a ON p.codigo = a.projeto
    ORDER BY p.codigo, a.codigo;
""")
resultados = cur.fetchall()
for row in resultados:
    print(f"Projeto {row[0]} - {row[1]} | Atividade {row[2]} - {row[3]}")

conn.commit()
cur.close()
conn.close()
print("\n=== CONEXÃO FECHADA ===")
