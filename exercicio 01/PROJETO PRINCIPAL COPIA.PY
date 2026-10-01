#SISTEMA PARA BIBLIOTECA
#Dados
Livros = []
Alunos = []

def lin_dup():
       print(("=" * 23))

def cadastrar_livros():
        print(f"\n=== CADASTRAR LIVRO  ===")
        codigo = input("Código do livro: ")
        titulo = input("titulo do livro: ")
        autor = input("Nome do autor: ")
        ano = int(input("Ano de publicação: "))
        quantidade = int(input("Quantidade disponível: "))

        livro = {"codigo" : codigo, "titulo" : titulo, "autor" : autor, "ano": ano, "quantidade": quantidade}
        Livros.append(livro)
        print("Livro cadastrado com sucesso!")
       
def listar_livros():
       print("\n=== LISTA DE LIVROS CADASTRADOS ===")

       if not Livros:
                print("Nenhum livro cadastrado até o momento.")

                for l in Livros:
                        print(f"Código: {l['codigo']} | Título: {l['titulo']} | Autor: {l['autor']} | Ano: {l['ano']} | Qtd: {l['quantidade']}")


      

while True:
#ENTRADA DE DADOS
        lin_dup()
        print( "SISTEMA PARA BIBLIOTECA")
        lin_dup()        
        print("1 - Cadastrar livros")
        print("2 - listar livros")
        print("3 - Pesquisar livros")
        print("4 - Cadastrar alunos")
        print("5 - Realizar emprestimo")
        print("6 - Sair")

        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            qtd = int(input("\nQuantos livros deseja cadastrar? "))
            for i in range(1, qtd +1):
                print(f"\n=== CADASTRAR LIVRO {i} ===")
                codigo = input("Código do livro: ")
                titulo = input("titulo do livro: ")
                autor = input("Nome do autor: ")
                ano = int(input("Ano de publicação: "))
                quantidade = int(input("Quantidade disponível: "))



                if codigo == "" :
                        print("Erro: O código está vazio.")
                elif titulo == "":
                        print("Erro: O título está vazio.")
                elif autor == "":
                        print("Erro: O autor está vazio.")
                elif ano <= 0:
                        print("Erro: O ano informado é inválido.")
                elif quantidade <= 0:
                        print("Erro: A quantidade disponível deve ser maior que zero.")
               
                else:
                        livro = {"codigo" : codigo, "titulo" : titulo, "autor" : autor, "ano": ano, "quantidade": quantidade}
                Livros.append(livro)
                print("Livro cadastrado com sucesso!")
                
                
                
        elif opcao == 2:
                print("\n=== LISTA DE LIVROS CADASTRADOS ===")
                if not Livros:
                        print("Nenhum livro cadastrado até o momento.")
                else:
                        for l in Livros:
                                print(f"Código: {l['codigo']} | Título: {l['titulo']} | Autor: {l['autor']} | Ano: {l['ano']} | Qtd: {l['quantidade']}")

        
        elif opcao == 3:
                print("\n === pesquisar livros ===")
                if not Livros:
                        print("Nenhum livro cadastrado encontrado até o momento.")

                busca = input("Digite o nome do livro que esta a buscar: ").lower(). strip()
                encontrados = []
                        
                for l in Livros:
                        if busca in l ['titulo']:
                                encontrados.append(l)    
                        if not encontrados:
                                print("Nenhum livro encontrado com esse título.")
                        else:
                                print(f"\nLivros encontrados ({len(encontrados)}):")
                for l in encontrados:
                    print(f"Código: {l['codigo']} | Título: {l['titulo']} | Autor: {l['autor']} | Ano: {l['ano']} | Qtd: {l['quantidade']}")
        
        elif opcao == 4:
            qtd_alunos = int(input("\nQuantos alunos deseja cadastrar? "))
            for i in range(1, qtd_alunos + 1):
                print(f"\n=== ALUNO {i} ===")
                matricula = input("Matrícula: ").strip()
                nome = input("Nome: ").strip()
                turma = input("Turma: ").strip()

                if matricula == "" or nome == "" or turma == "":
                    print("Erro: Todos os campos devem estar preenchidos.")
                else:
                    aluno = {
                        "matricula": matricula,
                        "nome": nome,
                        "turma": turma
                    }
                    Alunos.append(aluno)
                    print("\nALUNO CADASTRADO COM SUCESSO!")

        elif opcao == 5:
                print("\n=== EMPRESTIMO ===")
                codigo = input("Digite o código do livro: ")
                matricula = input("digite a Matrícula do aluno: ") 
                qtd = int(input("Quantidade dispónível? "))
   
                if codigo == "" or matricula == "":
                        print("Erro: Dados inválidos.")
                elif qtd <=0: 
                        print("\nNão é possível realizar o empréstimo.")
                        print( "Não há exemplares disponíveis.")
                else:
                        print("EMPRESTIMO REALIZADO COM SUCESSO!")
      
        elif opcao == 6:
                print("\nSaindo do sistema... Até logo!")

        else: 
                print("Opção inválida")
        