#SISTEMA PARA BIBLIOTECA
print("========================")
print( "SISTEMA PARA BIBLIOTECA")
print("========================")

#ENTRADA DE DADOS
cadastro_livros = []
cadastro_aluno = []

print("1 - Cadastrar livros")
print("2 - Cadastrar alunos")
print("3 - Realizar emprestimo")
print("4 - Sair")

while opcao <= 3:

    opcao = int(input("Escolha uma opção: "))
if opcao == 1:
    qtd = int(input("\nQuantos livros deseja cadastrar? "))
    for i in range(1, qtd +1):
        print(f"\n--- LIVRO {i}---")
        codigo = input("Código do livro: ")
        titulo = input("titulo do livro: ")
        autor = input("Nome do autor: ")
        ano = input("Ano de publicação: ")
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
                print("Livro cadastrado com sucesso!")

elif opcao == 2:
    qtd = int(input("\nQuantos alunos deseja cadastrar? "))
    for i in range(1, qtd +1):
        print(f"\n--- ALUNO {i} ---")
        matricula = int(input("Matrícula: "))
        nome = input("Nome: ")
        turma = input("Turma: ")

        if matricula == "" :
                print("Erro: Matricula está vazia.")
        elif nome == "":
                print("Erro: O nome está vazio.")
        elif turma == "":
                print("Erro: turma está vazia.")
        
        else:
                print("ALUNO CADASTRADO COM SUCESSO!")

elif opcao == 3:
    
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
      
elif opcao == 4:
    print("\nSaindo do sistema... Até logo!")

else: 
    print("Opção inválida")