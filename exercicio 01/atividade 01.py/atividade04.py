#Crie variáveis para nome, idade, curso, nota e aprovacao. Exiba todos os dados de forma organizada.
#cadastro de variáveis
nome = "Elias santos"
idade = 32
curso = "Educação Física"
nota = 8.5
aprovacao = True


#Imprimindo valores de aprovação
print("nome: ", nome)
print("idade: ", idade)
print("curso: ", curso)
print("nota: ", nota)
print("aprovacao: ", aprovacao)


if nota >= 7 and aprovacao == True:
    print("Você está aprovado!")
else:
    print("Você não está aprovado!")