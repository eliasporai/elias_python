Alunos = ["João", "Pedro", "José", "Maria"]

for contador in Alunos:
    print(contador)

#Variável para adicionar novos alunos
AdicionarAlunos =  int(input("QUANTOS ALUNOS DESEJA CADASTRAR?"))

for n in range(AdicionarAlunos):

    Alunos.append(input("informa o nome do aluno: "))

