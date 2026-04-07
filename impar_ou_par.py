import os

os.system("cls")

def impar_ou_par(resultado):

    os.system("cls")

    if numero % 2 ==0:
        
        print(f" {numero} é par")

    else:

        print(f" {numero} é impar ")



numero=int(input("Digite um numero "))

impar_ou_par(numero)