#Variaveis
Nome_do_produto = input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade disponível  do produto: "))

#regras de estoque
if quantidade == 0:
    situacao = "Produto esgotado"
elif  quantidade <=5:
    situacao = "Estoque crítico"
elif  quantidade <=20:
    situacao = "Estoque baixo"
else: 
    situacao = "Estoque normal"
    print("Estoque normal")


 #Saida de dados

print(f"Nome do produto: {Nome_do_produto}")
print(f"quantidade disponivel: {quantidade}")
print(f"situação do estoque: {situacao}")