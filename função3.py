import os 

os.system("cls")

# FUNÇÃO COM PARÂMETROS.
def somar(n1, n2):
    soma = n1 + n2
    print(f"Soma: {soma}")

# EXEMPLO DE USO DA FUNÇÃO.
primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))

# CHAMANDO A FUNÇÃO.
# ENVIANDO PARÂMETROS.
somar(primeiro_numero, segundo_numero)