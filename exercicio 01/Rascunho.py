#SISTEMA PARA BIBLIOTECA
#Dados
livros = []


print("========================")
print( "SISTEMA PARA BIBLIOTECA")
print("========================")

#ENTRADA DE DADOS
print("1 - Cadastrar livros")
print("2 - listar livros")
print("3 - Pesquisar livros")
print("4 - Cadastrar alunos")
print("5 - Realizar emprestimo")
print("6 - Sair")

opcao = int(input("\nEscolha uma opção: "))
if opcao == 1:
    qtd = int(input("\nQuantos livros deseja cadastrar? "))
    for i in range(1, qtd +1):
        print(f"\n=== LIVRO {i}===")
        codigo = int(input("Código do livro: "))
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

        #armazenamento do livro no sistema
                livro = {"codigo" : codigo, "titulo" : titulo, "autor" : autor, "ano": ano, "quantidade": quantidade}
                livros.append(livros)
                print("Livro cadastrado com sucesso!")

elif opcao == 2:
       print("\n=== LISTA DE LIVROS CADASTRADOS ===")
       if not livros:
                print("Nenhum livro cadastrado até o momento1")
                for i in range(len(livros)):
                    print(f"\nLivro #{i + 1}")  # Usamos i + 1 para começar a contagem em 1 no texto
                    print(f"Código: {livros[i]['codigo']}")
                    print(f"Título: {livros[i]['titulo']}")
                    print(f"Autor: {livros[i]['autor']}")
                    print(f"Ano: {livros[i]['ano']}")
                    print(f"Quantidade: {livros[i]['quantidade']}")