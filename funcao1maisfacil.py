import os 

# LIMPA O TERMINAL.
# CABEÇALHO.
# FUNÇÃO.
def logo_senai():
    os.system("cls")
    print("======== ========")
    print("   SENAI BAHIA   ")
    print("======== ========")

# CHAMAR A FUNÇÃO.
logo_senai()
nome = input("Digite seu nome: ")

logo_senai()
nome = int(input("Digite sua idade: "))

logo_senai()
nome = float(input("Digite seu peso: "))

