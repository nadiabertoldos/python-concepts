#Mensagens iniciais
#'Python' no terminal para testes
'''
Mensagens 
iniciais
'''
'''
print('Olá mundo!')
print('Olá, este (não) é o meu primeiro código em Python')
'''
# ------------------Tipos------------------ #
'''
#Tipo INT
idade = int(input('Digite sua idade: '))
print(f'Sua idade é {idade}')

#Tipo FLOAT
renda = float(input('Digite a sua renda: '))
print(f'Sua renda é de {renda}')

#Tipo STRING
nome = input('Digite seu nome: ')
print(f'Seu nome é {nome}')
'''
# ------------------Operações Matemáticas------------------ #
'''
#Soma
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
soma = n1 + n2
print(f'A soma dos valores é de {soma}')

#Subtração
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
sub = n1 - n2
print(f'A subtração dos valores é de {sub}')

#Multiplicação
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
mult = n1 * n2
print(f'A multiplicação dos valores é de {mult}')

#Divisão(retorna o resultado com uma casa após a vírgula)
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
div = n1 / n2 
print(f'A multiplicação dos valores é de {div}')

#Divisão inteira(não retorna o resultado com uma casa após a vírgula)
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
div_int = n1 // n2
print(f'A multiplicação dos valores é de {div_int}')
'''
# ------------------Operações resto (%), Incremento (+=) e Decremento(-=)------------------ #
'''
#Incremento
valor = 5
valor += 1
print(valor)

#Decremento
valor = 5
valor -= 1
print(valor)

#Resto
resto = 10 % 3
print(resto)
'''
# ------------------Ordem de Precedência------------------ #
'''
sem_ordem = 2 + 5 * 5
print(sem_ordem)

com_ordem = (2 + 5) * 5
print(com_ordem)
'''
# ------------------Operadores Relacionais------------------ #
'''
#Igual: ==
igual = 5 == 5 # and 6 == 4
print(igual)

#Maior: >
#Maior igual: >=
#Menor: <
#Menor igual: <=
#Diferente: !=
'''
# ------------------str.format()------------------ #
'''
valor = 45.00
print(f'{valor:.3f}') #quantidade de casas após a vírgula

print('Olá {}, você tem {} anos'.format('Nadia', 23))
'''