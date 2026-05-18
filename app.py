from pymongo import MongoClient
from datetime import datetime

# Configuração da conexão
MONGO_URI = "mongodb://admin:admin123@localhost:27017/"
DB_NAME = "AtividadesProj"

class GerenciadorAtividades:
    def __init__(self):
        try:
            self.client = MongoClient(MONGO_URI)
            self.db = self.client[DB_NAME]
            # Testar conexão
            self.client.admin.command('ping')
            print("✅ Conectado ao MongoDB com sucesso!\n")
        except Exception as e:
            print(f"❌ Erro ao conectar: {e}")
            exit(1)
    
    # CREATE - Inserir nova atividade
    def criar_atividade(self):
        print("\n--- NOVA ATIVIDADE ---")
        projeto_id = int(input("ID do projeto: "))
        
        # Verificar se projeto existe
        projeto = self.db.projetos.find_one({"projeto_id": projeto_id})
        if not projeto:
            print("❌ Projeto não encontrado!")
            return
        
        nome = input("Nome da atividade: ")
        descricao = input("Descrição: ")
        responsavel = int(input("ID do responsável: "))
        horas = int(input("Horas estimadas: "))
        
        # Buscar próximo ID
        ultima = self.db.atividades.find_one(sort=[("atividade_id", -1)])
        novo_id = (ultima["atividade_id"] + 1) if ultima else 1
        
        nova = {
            "atividade_id": novo_id,
            "projeto_id": projeto_id,
            "nome": nome,
            "descricao": descricao,
            "empregado_id_responsavel": responsavel,
            "horas_estimadas": horas,
            "status": "planejada",
            "data_criacao": datetime.now()
        }
        
        self.db.atividades.insert_one(nova)
        print(f"✅ Atividade '{nome}' criada com ID {novo_id}")
    
    # READ - Listar projetos com atividades
    def listar_tudo(self):
        print("\n--- PROJETOS E ATIVIDADES ---")
        projetos = self.db.projetos.find()
        
        for projeto in projetos:
            print(f"\n📁 PROJETO: {projeto['nome']}")
            print(f"   ID: {projeto['projeto_id']} | Líder: {projeto['lider_id']} | Status: {projeto['status']}")
            
            atividades = self.db.atividades.find({"projeto_id": projeto['projeto_id']})
            lista = list(atividades)
            
            if lista:
                for atv in lista:
                    print(f"   ▶ [{atv['status']}] {atv['nome']} ({atv['horas_estimadas']}h)")
            else:
                print("   📭 Nenhuma atividade")
    
    # UPDATE - Mudar líder do projeto
    def atualizar_lider(self):
        print("\n--- ATUALIZAR LÍDER ---")
        projeto_id = int(input("ID do projeto: "))
        novo_lider = int(input("Novo ID do líder: "))
        
        resultado = self.db.projetos.update_one(
            {"projeto_id": projeto_id},
            {"$set": {"lider_id": novo_lider}}
        )
        
        if resultado.modified_count > 0:
            print("✅ Líder atualizado!")
        else:
            print("❌ Projeto não encontrado ou líder já era esse")
    
    # DELETE - Remover atividade
    def remover_atividade(self):
        print("\n--- REMOVER ATIVIDADE ---")
        atividade_id = int(input("ID da atividade: "))
        
        resultado = self.db.atividades.delete_one({"atividade_id": atividade_id})
        
        if resultado.deleted_count > 0:
            print("✅ Atividade removida!")
        else:
            print("❌ Atividade não encontrada")
    
    def menu(self):
        while True:
            print("\n" + "="*40)
            print("1 - Criar atividade")
            print("2 - Listar projetos e atividades")
            print("3 - Atualizar líder de projeto")
            print("4 - Remover atividade")
            print("0 - Sair")
            
            opcao = input("\nEscolha: ")
            
            if opcao == "1":
                self.criar_atividade()
            elif opcao == "2":
                self.listar_tudo()
            elif opcao == "3":
                self.atualizar_lider()
            elif opcao == "4":
                self.remover_atividade()
            elif opcao == "0":
                print("Saindo...")
                break
            else:
                print("Opção inválida!")

if __name__ == "__main__":
    app = GerenciadorAtividades()
    app.menu()
