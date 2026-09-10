#VARIÁVEIS
nome_do_cliente = input("Digite o nome do cliente: ")
velocidade_contratada = float(input("Digite a velocidade contratada em Mbps: "))

#regras de negócio
if velocidade_contratada <= 50:
    plano = "Plano Básico"
elif velocidade_contratada <=199:
    plano = "Plano Intermediário"
elif velocidade_contratada <= 499:
    plano = "Plano Ultra"
else: 
    plano = "plano inexistente"
    print("Velocidade contratada inválida. Por favor, insira uma velocidade válida.")

 #Saída de dados
 
print(f"nome do cliente: {nome_do_cliente}")
print(f"velocidade contratada: {velocidade_contratada} Mbps")
print(f"plano contratado: {plano}")