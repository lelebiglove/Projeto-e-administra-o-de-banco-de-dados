from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, text
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

# Conexão com o banco
engine = create_engine('postgresql://lelebiglove:senha123@localhost:5432/atividade_db')
Base = declarative_base()

# Definição das classes
class Projeto(Base):
    __tablename__ = 'projeto'
    codigo = Column(Integer, primary_key=True)
    nome = Column(String(50))
    descricao = Column(String(250))
    responsavel = Column(Integer)
    depto = Column(Integer)
    data_inicio = Column(Date)
    data_fim = Column(Date)
    atividades = relationship("Atividade", back_populates="projeto_rel")

class Atividade(Base):
    __tablename__ = 'atividade'
    codigo = Column(Integer, primary_key=True)
    descricao = Column(String(250))
    projeto = Column(Integer, ForeignKey('projeto.codigo'))
    data_inicio = Column(Date)
    data_fim = Column(Date)
    projeto_rel = relationship("Projeto", back_populates="atividades")

# Criar sessão
Session = sessionmaker(bind=engine)
session = Session()

# 1. Inserir uma atividade
print("=== INSERINDO ATIVIDADE COM ORM ===")
nova_atividade = Atividade(
    descricao='Nova Atividade - Teste ORM',
    projeto=2,
    data_inicio='2024-02-01',
    data_fim='2024-08-31'
)
session.add(nova_atividade)
session.flush()
print(f"Atividade inserida: Código={nova_atividade.codigo}, Descrição={nova_atividade.descricao}")

# 2. Atualizar líder do projeto
print("\n=== ATUALIZANDO LÍDER COM ORM ===")
projeto = session.query(Projeto).filter_by(codigo=4).first()
print(f"Projeto {projeto.nome} - Responsável antigo: {projeto.responsavel}")
projeto.responsavel = 2
print(f"Projeto {projeto.nome} - Novo responsável: {projeto.responsavel}")

# 3. Listar projetos e atividades
print("\n=== PROJETOS E ATIVIDADES COM ORM ===")
projetos = session.query(Projeto).order_by(Projeto.codigo).all()
for p in projetos:
    for a in p.atividades:
        print(f"Projeto {p.codigo} - {p.nome} | Atividade {a.codigo} - {a.descricao}")

session.commit()
session.close()
print("\n=== CONEXÃO ORM FECHADA ===")


