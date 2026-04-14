import os 

os.system("cls")


def Ano_nascimento(ano_nasceu):

    idade= 2026 - ano_nasceu

    return idade


i=int(input("Digite sua data de nascimento."))

resposta=Ano_nascimento(i)

print(f" A sua idade é : {resposta}")