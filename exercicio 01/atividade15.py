#Salário
#dados de entrada
salario_atual = float(input("Digite o salário atual(R$): "))
pecentual_reajuste = float(input("Digite o percentual de reajuste(%): "))

#calculo do novo salário
valor_reajuste = salario_atual * (pecentual_reajuste / 100)
novo_salario = salario_atual + valor_reajuste

#exibindop o resultado
print(f"\nValor do reajuste: R$ {valor_reajuste:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")