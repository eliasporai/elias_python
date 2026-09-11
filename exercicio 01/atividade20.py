#Calculadora
#variáveis
num1 = float(input("digite o primeiro numero: "))
num2 = float(input("digite o segundo numero: "))

#regras 
print("soma: ", num1 + num2)
print("subtração: ", num1 - num2)
print("multiplicação: ", num1 * num2)

if num2 != 0:
    print("divisão: ", num1 / num2)
else:
    print("divisão não é possivel por 0")
