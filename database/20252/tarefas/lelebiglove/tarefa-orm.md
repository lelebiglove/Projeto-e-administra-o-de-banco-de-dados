# Tarefa - ODBC e ORM

**Aluna:** Leandro Isaac Correia de Brito 
**Matrícula:** 20240028406  
**Email:** isaac.brito.136@ufrn.edu.br  
**GitHub:** lelebiglove

---

## Links

- [Script SQL](../../../../scripts/atividades.sql)
- [Programa ODBC](../../../../conexao_odbc.py)
- [Programa ORM](../../../../conexao_orm.py)

---

## Resumo sobre ODBC em Python

ODBC (Open Database Connectivity) é uma API padrão para acessar bancos de dados. Em Python, utilizei o pacote **psycopg2** como driver para conectar ao PostgreSQL.

### Funcionamento:
- Estabelece conexão direta com o banco usando credenciais
- Executa comandos SQL diretamente via cursor
- É necessário gerenciar manualmente conexões, cursores e transações
- Oferece controle total sobre as queries SQL

### Vantagens:
- Controle direto sobre o SQL
- Performance otimizada
- Suporte a todos os recursos do PostgreSQL

---

## Resumo sobre ORM em Python

ORM (Object-Relational Mapping) mapeia tabelas do banco para objetos Python. Utilizei o framework **SQLAlchemy**, o mais popular ORM para Python.

### Funcionamento:
- Define classes Python que representam tabelas
- Relacionamentos são definidos como atributos
- Operações CRUD são feitas através de objetos, sem SQL explícito

### Framework: SQLAlchemy
- **Engine:** Gerencia a conexão com o banco
- **Base:** Classe base para modelos declarativos
- **Session:** Gerencia transações e operações
- Suporta lazy loading e eager loading de relacionamentos

### Vantagens:
- Código mais limpo e orientado a objetos
- Independência do banco de dados
- Gerenciamento automático de relacionamentos
- Segurança contra SQL Injection

