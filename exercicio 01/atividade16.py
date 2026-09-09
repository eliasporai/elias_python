#Desconto
#dados de entrada
preço_produto = float(input("digte o preço do produto: "))
desconto = float(input("digite o percentual de desconto(%): "))

#claculo do valor do desconto
valor_do_desconto = preço_produto * (desconto / 100)

#calculo do preço final do produto
preço_final = preço_produto - valor_do_desconto

print(f"\nValor do desconto: R$ {valor_do_desconto:.2f}")
print(f"Preço final do produto: R$ {preço_final:.2f}")
