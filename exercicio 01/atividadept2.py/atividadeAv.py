livros = []
while True:
    
    print("\n===== BIBLIOTECA =====")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Pesquisar livro")
    print("4 - Excluir livro")
    print("5 - Saber quantos livros estão cadastrados.")
    print("6 - Sair")

    opcao = input("Digite uma opção: ")

    if opcao == "1":

        titulo = input("Digite o título: ")
        autor = input("Digite o autor: ")
        
        livros.append([titulo, autor])

        print("Livro cadastrado!")
    
    elif opcao == "2":
        
        print("\n--- LIVROS CADASTRADOS ---")

        for contador in livros:
            print("Título:", contador[0])
            print("Autor:", contador[1])
    
    elif opcao == "3":

        pesquisa = input("Digite o título que deseja pesquisar: ")
        encontrado = False

        for contador in livros:
            if contador[0] == pesquisa:
                print("Livro encontrado!")
                print("Título:", contador[0])
                print("Autor:", contador[1])
                encontrado = True
            break

        if not encontrado:
            print("Livro não encontrado!")

    elif opcao == "4":

        pesquisa = input("Digite o título que deseja excluir: ")
        encontrado = False

        for contador in livros:
            if contador[0].lower() == pesquisa.lower():

                livros.remove(contador)
                print("Livro excluído!")
                encontrado = True
                break
        if not encontrado:
            print("Livro não encontrado para exclusão.")

    elif opcao == "5":
        total_livros = len(livros)
        print(f" Total de livros cadastrados: {total_livros}")

    elif opcao == "6":
        print("Programa encerrado.")
        break

    else:

        print("Opção inválida!")