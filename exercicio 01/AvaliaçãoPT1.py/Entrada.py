biblioteca = []
aluno = []
emprestimo = []

#SISTEMA PARA BIBLIOTECA

def lin_dup():
       print(("=" * 23))




#ENTRADA DE DADOS
def exibir_menu ():
        lin_dup()
        print( "SISTEMA PARA BIBLIOTECA")
        lin_dup()
        print("1 - Cadastrar livros")
        print("2 - listar livros")
        print("3 - Pesquisar livros")
        print("4 - Cadastrar alunos")
        print("5 - Realizar emprestimo")
        print("6 - Sair")


exibir_menu()

#"""Lê os dados e insere o livro como um dicionário na lista biblioteca."""
def cadastrar_livro():      
        titulo = input("Título: ")
        autor = input("Autor: ")
        livro = [titulo, autor]
        biblioteca.append(livro)

def listar_livros():
        for contador in biblioteca:
                print (contador[0], ".", contador[1])

while True:
        print("\n cadastrar Livro")
        