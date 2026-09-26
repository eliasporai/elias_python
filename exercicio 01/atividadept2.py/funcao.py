#função

#ef saudacao():
#   print("Estude Python")

#Chamando a função
#cls
# acao()

#outra foema de fazer a mesma ação:
#declarando uma função que irá receber um parametro nomeado

#ef saudacao_com_parametro(recebe_mensagem):
#   print(recebe_mensagem)
#
#
#   def multiplicar_por_7:

def verificar_estoque(quantidade):
    if quantidade > 0:
        return "Disponível"
    return "Indisponível"
situacao = verificar_estoque(0)
print(situacao)