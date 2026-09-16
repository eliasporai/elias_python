#Expressão lógica
#VARIÁVEIS
idade = int(input("Digite sua idade: "))
curso_tecnico = (input(" Possui curso técnico? (sim /não): ")).lower() == 'sim'

#regras 
if idade >= 18 and curso_tecnico: 
    print("apto ao trabalhao")
elif idade >= 18 and not curso_tecnico:
    print("inapto ao trabalho")
elif idade < 18 and curso_tecnico:
    print("idade inapta ao trabalho")
else:
    print("inaptoao trabalho")