# Tarefa - MongoDB

**Nome:** Andro Isaac Correia de Brito  
**Matrícula:** 20240028406  
**Email:** isaac.brito.136@ufrn.edu.br  

## Links

- [Programa CRUD (app.py)](app.py)
- [Script de inicialização do MongoDB](scripts/init-mongo.js)
- [Docker Compose](scripts/docker-compose-mongo.yml)

---

## Resumo sobre MongoDB
### O que é MongoDB?

MongoDB é um SGBD NoSQL orientado a documentos. Diferente de bancos relacionais que usam tabelas, o MongoDB armazena dados em **documentos JSON** agrupados em **coleções**.

### Principais características:

| Característica | Descrição |
|----------------|-----------|
| **Schema flexível** | Documentos na mesma coleção podem ter estruturas diferentes |
| **Escalabilidade horizontal** | Distribui dados entre servidores (sharding) |
| **Alta disponibilidade** | Replica Sets garantem redundância |
| **Indexação** | Índices para consultas eficientes |
| **Aggregation Pipeline** | Framework para transformação de dados |

---

## Replica Sets

### O que é?

Um **Replica Set** é um grupo de servidores MongoDB que mantêm os mesmos dados, garantindo alta disponibilidade.

### Papéis dos membros:

| Papel | Função |
|-------|--------|
| **Primário (Primary)** | Recebe todas as escritas. Apenas um por Replica Set |
| **Secundário (Secondary)** | Réplica apenas-leitura. Assume se primário falhar |
| **Arbiter (Árbitro)** | Não armazena dados. Só vota em eleições para desempatar |

Se o primário falha, os secundários realizam uma **eleição** e um deles se torna o novo primário automaticamente.

---

## Operações CRUD implementadas

| Operação | Função no programa | Descrição |
|----------|-------------------|-----------|
| **Create** | `criar_atividade()` | Insere nova atividade em projeto existente |
| **Read** | `listar_tudo()` | Lista projetos com suas atividades |
| **Update** | `atualizar_lider()` | Altera o líder de um projeto |
| **Delete** | `remover_atividade()` | Remove uma atividade de um projeto |

---

## Como executar o programa

```bash
# Ativar ambiente virtual
source venv/bin/activate

# Executar
python3 app.py
