import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class Funcionario:
    nome: str
    idade: int

    def mostrar_dados(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}\n')


QUANTIDADE_FUNCIONARIOS = 2
lista_funbcionarios = []

print('= Solicitando dados =')
for i in range(QUANTIDADE_FUNCIONARIOS):
    novo_funcionario = Funcionario (
        nome=input('Digite seu nome: '),
        idade=int(input('Digite sua idade: '))
    )
    print('')
    lista_funbcionarios.append(novo_funcionario)

print('= Exibindo dados =')
for funcionario in lista_funbcionarios:
    funcionario.mostrar_dados()

print('= Salvando dados =')
with open('lista_funcionarios.csv', 'a') as arquivo:
    for funcionario in lista_funbcionarios:
        arquivo.write(f'{funcionario.nome}, {funcionario.idade}\n')
    print('Salvo com sucesso!!')

print('= Fim do programa. =')