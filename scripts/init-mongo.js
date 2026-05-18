// Aguardar o MongoDB iniciar
sleep(5000);

// Configurar o Replica Set
rs.initiate({
  _id: "rs0",
  members: [{ _id: 0, host: "localhost:27017" }]
});

// Aguardar eleição do primário
sleep(5000);

// Criar banco e usuário da aplicação
db = db.getSiblingDB('AtividadesProj');

db.createUser({
  user: "app_user",
  pwd: "app_password123",
  roles: [{ role: "readWrite", db: "AtividadesProj" }]
});

// Criar coleções
db.createCollection('empregados');
db.createCollection('projetos');
db.createCollection('atividades');

// Inserir empregados
db.empregados.insertMany([
  { empregado_id: 1, nome: "Ana Silva", cargo: "Gerente de Projetos", email: "ana@empresa.com" },
  { empregado_id: 2, nome: "Carlos Souza", cargo: "Desenvolvedor Senior", email: "carlos@empresa.com" },
  { empregado_id: 3, nome: "Mariana Costa", cargo: "Líder Técnica", email: "mariana@empresa.com" },
  { empregado_id: 4, nome: "Pedro Oliveira", cargo: "Desenvolvedor", email: "pedro@empresa.com" }
]);

// Inserir projetos
db.projetos.insertMany([
  { projeto_id: 1, nome: "Sistema de Vendas", lider_id: 1, data_inicio: new Date("2025-01-01"), status: "ativo" },
  { projeto_id: 2, nome: "App Mobile", lider_id: 3, data_inicio: new Date("2025-02-01"), status: "ativo" },
  { projeto_id: 3, nome: "Dashboard Analytics", lider_id: 2, data_inicio: new Date("2025-03-01"), status: "planejado" }
]);

// Inserir atividades
db.atividades.insertMany([
  { atividade_id: 1, projeto_id: 1, nome: "Levantamento de Requisitos", descricao: "Reuniões com stakeholders", empregado_id_responsavel: 1, horas_estimadas: 40, status: "concluida" },
  { atividade_id: 2, projeto_id: 1, nome: "Desenvolvimento Backend", descricao: "API REST", empregado_id_responsavel: 2, horas_estimadas: 160, status: "em_andamento" },
  { atividade_id: 3, projeto_id: 2, nome: "Design de Interface", descricao: "Protótipos Figma", empregado_id_responsavel: 4, horas_estimadas: 80, status: "em_andamento" },
  { atividade_id: 4, projeto_id: 2, nome: "Desenvolvimento Mobile", descricao: "React Native", empregado_id_responsavel: 4, horas_estimadas: 200, status: "planejada" },
  { atividade_id: 5, projeto_id: 3, nome: "Configuração do Ambiente", descricao: "Setup Data Warehouse", empregado_id_responsavel: 2, horas_estimadas: 60, status: "planejada" }
]);

print("✅ Banco AtividadesProj inicializado com sucesso!");

