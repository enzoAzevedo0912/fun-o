import os

os.system("cls")

# FUNÇÃO COM PARÂMETROS.
def saudacao(nome):
    print(f"Olá, {nome}!")
    print("Bem-Vindo(a) ao nosso site!")


# EXEMPLO DE USO DA FUNÇÃO.
nome_visitante = input("Digite seu nome: ")
saudacao(nome=nome_visitante)