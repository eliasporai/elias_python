# SISTEMA PARA BIBLIOTECA SIMPLES

Livros = []
Alunos = []

def lin_dup():
    print("=" * 23)

def cadastrar_livro():
    print("\n=== CADASTRAR LIVRO ===")
    codigo = input("Código: ")
    titulo = input("Título: ")
    autor = input("Autor: ")
    ano = int(input("Ano: "))
    quantidade = int(input("Quantidade: "))
    
    livro = {"codigo": codigo, "titulo": titulo, "autor": autor, "ano": ano, "quantidade": quantidade}
    Livros.append(livro)
    print("Livro cadastrado com sucesso!")

def listar_livros():
    print("\n=== LISTA DE LIVROS ===")
    if not Livros:
        print("Nenhum livro cadastrado.")
    for l in Livros:
        print(f"Código: {l['codigo']} | Título: {l['titulo']} | Qtd: {l['quantidade']}")

def pesquisar_livro():
    print("\n=== PESQUISAR LIVRO ===")
    busca = input("Digite o título: ").lower()
    encontrou = False
    for l in Livros:
        if busca in l['titulo'].lower():
            print(f"Encontrado: {l['titulo']} (Código: {l['codigo']})")
            encontrou = True
    if not encontrou:
        print("Livro não encontrado.")

def cadastrar_aluno():
    print("\n=== CADASTRAR ALUNO ===")
    matricula = input("Matrícula: ")
    nome = input("Nome: ")
    
    aluno = {"matricula": matricula, "nome": nome}
    Alunos.append(aluno)
    print("Aluno cadastrado com sucesso!")

def realizar_emprestimo():
    print("\n=== EMPRÉSTIMO ===")
    cod = input("Código do livro: ")
    mat = input("Matrícula do aluno: ")
    
    for l in Livros:
        if l['codigo'] == cod:
            if l['quantidade'] > 0:
                l['quantidade'] -= 1
                print("Empréstimo realizado com sucesso!")
                return
            else:
                print("Livro sem exemplares disponíveis.")
                return
    print("Livro não encontrado.")

# PROGRAMA PRINCIPAL
while True:
    lin_dup()
    print("SISTEMA PARA BIBLIOTECA")
    lin_dup()        
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Pesquisar livro")
    print("4 - Cadastrar aluno")
    print("5 - Realizar empréstimo")
    print("6 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        cadastrar_livro()
    elif opcao == 2:
        listar_livros()
    elif opcao == 3:
        pesquisar_livro()
    elif opcao == 4:
        cadastrar_aluno()
    elif opcao == 5:
        realizar_emprestimo()
    elif opcao == 6:
        print("Saindo...")
        break
    else:
        print("Opção inválida.")