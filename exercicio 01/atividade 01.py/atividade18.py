#COMPARAÇÕES
#Variáveis

Nascimento = int(input("Digite seu ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))

#Regras de negócio  
if Nascimento  == 2008:
    situacao = "Você tem 18 anos"
elif Nascimento >=2007:
    situacao = "Você é menor de idade"
else: 
    situacao = "Maior de idade"

#saida de dados

print(f"sua situação é: {situacao}")
