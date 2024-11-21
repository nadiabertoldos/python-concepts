#------Perguntas sobre um crime------
#Utilizando listas, faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#- "Telefonou para a vítima?"
#- "Esteve no local do crime?"
#- "Mora perto da vítima?"
#- "Devia para a vítima?"
#- "Já trabalhou com a vítima?"
#O programa deve, no final, emitir uma classificação sobre a participação da pessoa no crime:
#- Respostas positivas para 2 questões: "Suspeita".
#- Respostas positivas entre 3 e 4 questões: "Cúmplice".
#- Respostas positivas para 5 questões: "Assassino".
#- Caso contrário, será classificada como "Inocente".
perguntas = []
positiva = []

resposta = input("Telefonou para a vítima?: ")
perguntas.append(resposta)

resposta = input("Esteve no local do crime?: ")
perguntas.append(resposta)

resposta = input("Mora perto da vítima?: ")
perguntas.append(resposta)

resposta = input("Devia para a vítima?: ")
perguntas.append(resposta)

resposta = input("Já trabalhou com a vítima?: ")
perguntas.append(resposta)

for i in perguntas:
    if i.lower() == 'sim':
        positiva.append(i)

if len(positiva) == 2:
    print('Suspeito')
elif len(positiva) == 3 or len(positiva) == 4:
    print('Cúmplice')
elif len(positiva) == 5:
    print('Assassino')
else:
    print('Inocente')

#------Notas dos alunos------
#Faça um programa que:
#- Peça as quatro notas de 5 alunos.
#- Calcule e armazene em uma lista a média de cada aluno.
#- Imprima o número de alunos com média maior ou igual a 7.0.
medias_alunos = []
alunos = 5
media_maior = []

for i in range(alunos):
    n1 = int(input(f'\nInforme a primeira nota do aluno {i+1}: '))
    n2 = int(input(f'Informe a segunda nota do aluno {i+1}: '))
    n3 = int(input(f'Informe a terceira nota do aluno {i+1}: '))
    n4 = int(input(f'Informe a quarta nota do aluno {i+1}: '))
    
    media = (n1 + n2 + n3 + n4) / 4
    medias_alunos.append(media)

for i in medias_alunos:
    if i >= 7:
        media_maior.append(i)

print(f'\nHá {len(media_maior)} alunos com média maior ou igual a 7.0')

#------Carrinho de compras------
#Crie um dicionário representando um carrinho de compras. Adicione produtos (chaves) e suas quantidades (valores) ao carrinho. Calcule o total de itens no carrinho de compras.
compras = {}
compras['Arroz'] = 21.99
compras['Detergente'] = 5.49
compras['Sabonete'] = 1.00
compras['Leite'] = 6.25
compras['Manteiga'] = 7.00

print(f'Há {len(compras)} itens no carrinho de compras:\n{compras.keys()}')

#------Contatos------
#Crie um dicionário representando contatos (nome, telefone). Permita ao usuário procurar por um contato pelo nome.
contatos = {}
contatos['Nadia'] = 1198756542
contatos['Julia'] = 1197463215
contatos['Deivid'] = 1299523677
contatos['Camila'] = 1192547611

info = input('Digite o nome do contato: ')

for key,value in contatos.items():
    if key.lower() == info.lower():
        print(f'Nome: {key}\nContato: {value}')

#------Concatenar tuplas------
#Crie duas tuplas e concatene-as para formar uma nova tupla.
nome1 = ('Nadia')
nome2 = ('Camila')

nomes = (nome1, nome2)

print(nomes)
'''
'''
nome1 = 'abc'
nome2 = 'def'

nomes = nome1 + nome2

print(nomes)

#------Nome invertido------
#Faça um programa que:
#- Permita ao usuário digitar o seu nome.
#- Mostre o nome do usuário de trás para frente, utilizando somente letras maiúsculas.
#- Dica: Lembre-se de que o usuário pode digitar o nome com letras maiúsculas ou minúsculas.
nome = input('Digite o seu nome: ')
print(nome.upper()[::-1])
