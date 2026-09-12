#SISTEMA PARA BIBLIOTECA
print("========================")
print( "SISTEMA PARA BIBLIOTECA")
print("========================")

#ENTRADA DE DADOS
print("1 - Cadastrar livros")
print("2 - Cadastrar alunos")
print("3 - Realizar emprestimo")
print("4 - Sair")

opcao = int(input("escolha uma opção: "))

if opcao == 1:
    qtd = int(input("\nQuantos livros deseja cadastrar? "))
    for i in range(1, qtd +1):
        print(f"--- LIVRO{i}---")
        codigo = input("Código do livro: ")
        titulo = input("titulo do livro: ")
        autor = input("Nome do autor: ")
        ano = input("Ano de publicação: ")
        quantidade = int(input("Quantidade disponível: "))

        if titulo == "" or autor == "" or ano == "" or quantidade <=0:
            print("Dados inválidos")
        else: 
            print("LIVRO CADASTRADO COM SUCESSO!")

elif opcao == 2:
    qtd = int(input("\nQuantos alunos deseja cadastrar? "))
    for i in range(2, qtd +2):
        print(f"--- ALUNO{i}---")
        matricula = int(input("Matrícula: "))
        nome = input("Nome: ")
        turma = input("Turma: ")

        print("ALUNO CADASTRADO COM SUCESSO!")

elif opcao == 3:
    
    print("=== EMPRESTIMO ===")
    codigo = input("Digite o código do livro: ")
    matricula = input("digite a Matrícula do aluno: ") 
    qtd = int(input("Quantidade dispónível? "))

    print("Emprestimo realizado com Sucesso, boa leitura!")      
elif opcao == 4:
    print("\nSaindo do sistema... Até logo!")

else: 
    print("Opção inválida")
