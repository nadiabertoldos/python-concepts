import datetime as dt

#------Operações matemáticas básicas------
#Faça um programa que peça dois números, realize as principais operações: soma, subtração, multiplicação, divisão.
a = int(input("Digite o valor a: "))
b = int(input("Digite o valor b: "))

soma = a + b
sub = a - b
mult = a * b
div = a / b

print('Soma: ', soma)
print('Subtração: ', sub)
print('Multiplicação: ', mult)
print('Divisão: ', div)

#------Cálculo da idade------
#2 - Peça ao usuário para informar o ano de nascimento. Em seguida, calcule e imprima a idade atual.
ano_nasc = int(input('Informe o seu ano de nascimento: '))
idade = dt.date.today().year - ano_nasc 
print(idade)

#------Conversão de quilômetros------
#Faça um programa que peça a quantidade de quilômetros, transforme em metros, centímetros e milímetros.
valor = float(input('Informa a quantidade de kms: '))

km = valor * 1000
cm = valor * 100000
mm = valor * 1000000

print('km: ', km)
print('cm: ', cm)
print('mm: ', mm)

#------Cálculo de consumo médio------
#Receba do usuário a quantidade de litros de combustível consumidos e a distância percorrida. Calcule e imprima o consumo médio em km/l.
quant_litros = float(input('Informe a quantidade de combustível consumida em litros: ')) 
dist_percorrida = float(input('Informe a distância percorrida: ')) 

consumo =  dist_percorrida / quant_litros

print(f'O consumo médio foi de {consumo} km/l')

#------Comparativo de tempos de viagem------
#Escreva um programa que calcule o tempo de uma viagem. Faça um comparativo do mesmo percurso de avião, carro e ônibus, levando em consideração:
#- Avião = 600 km/h
#- Carro = 100 km/h
#- Ônibus = 80 km/h
distancia = int(input('Informe a distância percorrida em kms: '))

aviao = distancia/600
carro = distancia/100
onibus = distancia/80

print(f'O tempo da viagem de avião será de {aviao: .1f} horas')
print(f'O tempo da viagem de carro será de {carro: .1f} horas')
print(f'O tempo da viagem de ônibus será de {onibus: .1f} horas')

#------Cálculo do Índice de Massa Corporal (IMC)------
#Solicite ao usuário o peso em kg e a altura em metros. Calcule e imprima o Índice de Massa Corporal (IMC) usando a fórmula: IMC = peso / (altura x altura).
peso = float(input('Informe o seu peso: '))
altura = float(input('Informe sua altura: '))

imc = peso / (altura * altura)

print(f'Seu IMC é: {imc: .2f}')

#------Cálculo do salário mensal------
#Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
valor_hora = float(input('Informe quanto você ganha por hora: '))
horas_trab = int(input('Informe a quantidade de horas trabalhadas no mês: '))

salario = valor_hora * horas_trab

print(f'Seu salário será: {salario: .2f}')

#------Cálculo de calorias queimadas em exercícios------
#Solicite ao usuário o número de horas de exercício físico por semana. Calcule o total de calorias queimadas em um mês, considerando uma média de 5 calorias por minuto de exercício.
horas_exec = float(input('Informe o número de horas que você realiza exercícios físicos por semana: '))

quant_min = horas_exec * 60
calorias = (quant_min * 5) * 4 #4 semanas

print(f'Total de calorias queimadas em um mês: {calorias: .2f}')

#------Mensagem personalizada------
#Faça um programa que utilize 4 variáveis como preferir e, no final, exiba uma mensagem amigável utilizando as variáveis criadas. Exemplos de variáveis: nome, idade, lugar, profissão. Exemplo de retorno: "Olá Maria, prazer te conhecer. Sou de São Paulo também e estou migrando de área."
nome = input("Informe o seu nome: ")
idade = input("Informe a sua idade: ")
cidade = input("Informe a sua cidade: ")
profissao = input("Informe a sua profissão: ")

print(f"Olá {nome}, prazer te conhecer! Vejo que você tem {idade} anos e é de {cidade}. Que legal que você trabalha como {profissao}!")