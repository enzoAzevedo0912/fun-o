import os 

os.system("cls")


def tabuada(numero):

    for i in range(11):



        Resultado = numero_da_tabuada * i

        print(f" {numero_da_tabuada} * {i} == {Resultado}")



while True:

    numero_da_tabuada=int(input("Digite um numero: "))

    tabuada(numero_da_tabuada)