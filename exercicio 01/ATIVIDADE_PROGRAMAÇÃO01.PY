#SOLICITAÇÃO DE CHAMAODOS   
#entrada de dados
nome_de_usuario = input("Digite o nome do usuário: ")
tempo_de_problema = int(input("Digite o tempo de problema em minutos: "))

print("selecione o tipo de problema:")
print("1 - Indisponibilidade total do sistema")
print("2 - Sistema funcionando, mas com lentidão ou erros")
print("3 - Problema que não impede o trabalho")
print("4 - Outros problemas")

opcao = int(input("Digite a opção identificada: "))

#definição de prioridade com base na opção escolhida
if opcao == 1:
    tipo_problema = "Indisponibilidade total do sistema"
    prioridade = "Critica"
elif opcao == 2:
    tipo_problema = "Sistema funcionando, mas com lentidão ou erros"
    prioridade = "Alta"
elif opcao == 3:
    tipo_problema = "Problema que não impede o trabalho"
    prioridade = "Média"
else:
    tipo_problema = "Outros problemas"
    prioridade = "Baixa"

#saida de resultados
print("\nResumo do Chamado:")
print(f"Nome do usuário: {nome_de_usuario}")
print(f"Tipo de problema: {tipo_problema}")
print(f"Prioridade: {prioridade}")

#resposta ao chamado com base na prioridade do chmado
if opcao == 1:
    print("Resposta: Recebemos seu chamado e seu problema será resolvido em até 15 minutos.")
elif opcao == 2:
    print("Resposta: Recebemos seu chamado e seu problema será resolvido em até 30 minutos.")
elif opcao == 3:
    print("Resposta: Recebemos seu chamado e seu problema será resolvido em até 45 minutos.")
else:
    print("Resposta: Recebemos seu chamado e seu problema será resolvido em até 24 horas.")
