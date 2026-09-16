#DIVISÃO DE DOIS NÚMEROS
#variaveis
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

#regras de negócio

if numero2 == 0:
    print("Erro: Divisão por zero não é permitida.")

quocinete = numero1 / numero2
divisão_inteira = numero1 // numero2
resto = numero1 % numero2

print(f"Quocinete: {quocinete}")
print(f"Divisão inteira: {divisão_inteira}")
print(f"Resto: {resto}")
