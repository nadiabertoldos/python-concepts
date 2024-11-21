#------Maior número entre dois valores------
#Faça um programa que peça dois números e imprima o maior deles.
num1 = int(input("Informe um valor: "))
num2 = int(input("Informe outro valor: "))

if num1 > num2:
    print(num1)
else:
    print(num2)

#------Saudação por turno de estudo------
#Faça um programa que pergunte em que turno você estuda. Peça para digitar:
#- M para Matutino
#- V para Vespertino
#- N para Noturno
#Imprima a mensagem correspondente:
#- "Bom Dia!"
#- "Boa Tarde!"
#- "Boa Noite!"
#- "Valor Inválido!"
print("Selecione o turno em que você estuda: ")
turno = input('M: Matutino \nV: Vespertino\nN: Noturno\n')

if turno == 'M' or turno == 'm':
    print('Bom dia!')
elif turno == 'V' or turno == 'v':
    print('Boa tarde!')
elif turno == 'N' or turno == 'n':
    print('Boa noite!')
else:
    print('Valor Inválido!')

#------Validação de nota------
#Faça um programa que peça uma nota entre 0 e 10. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
nota = -1
while nota < 0 or nota > 10:
    nota = int(input('Digite a nota: '))
    if nota < 0 or nota > 10:
        print('Valor inválido! A nota deve ser entre 0 e 10.')
print('Sucesso!')
'''
'''
while True:
    try:
        nota = int(input('Digite a nota: '))
        if nota >= 0 and nota <= 10:
            print('Sucesso!')
            break
        else:
            print('Valor inválido! A nota deve estar entre 0 e 10.')
    except ValueError:
        print('Entrada inválida! Por favor, insira um número inteiro.')

#------Classificação de aluno------
#Implemente um programa que classifique um aluno com base em sua pontuação em um exame. O programa deverá solicitar uma nota de 0 a 10. Se a pontuação for maior ou igual a 7, o aluno é aprovado. Caso contrário, ele é reprovado.
nota = int(input('Digite a nota: '))
if nota >= 7 and nota <= 10:
    print('Aprovado!')
elif nota < 7 and nota >= 0:
    print('Reprovado!')
else:
    print('Valor inválido! A nota deve estar entre 0 e 10.')

#------Classificação de triângulos------
#Desenvolva um programa que solicite ao usuário os comprimentos dos três lados de um triângulo e classifique-o como:
#- Equilátero: todos os lados com o mesmo valor.
#- Isósceles: dois lados com o mesmo valor.
#- Escaleno: todos os lados com medidas distintas.
print('---Classificação de Triângulos---')
a = int(input('Informe o comprimento do primeiro lado: '))
b = int(input('Informe o comprimento do segundo lado: '))
c = int(input('Informe o comprimento do terceiro lado: '))

if a == b and b == c:
    print('Triângulo Equilátero')
elif a == b or b == c or a == c:
    print('Triângulo Isósceles')
elif a != b and b != c and c != a:
    print('Triângulo Escaleno')

#------Login e senha------
#Crie um programa que solicite ao usuário um login e uma senha. O programa deve permitir o acesso apenas se:
#O usuário for "admin" e a senha for "admin123". Caso contrário, imprima uma mensagem de erro.
while True:
    login = input('Digite o login: ')
    senha = input('Digite a senha: ')
    if login == 'admin' and senha == 'admin123':
        print('Login efetuado com sucesso!')
        break
    else:
        print('Login e/ou senha incorretos. Tente novamente.')
'''
'''
login = input('Digite o login: ')
senha = input('Digite a senha: ')
if login == 'admin' and senha == 'admin123':
    print('Login efetuado com sucesso!')
else:
    print('Login e/ou senha incorretos.')

#------Classificação por idade------
#Desenvolva um programa que solicite a idade do usuário e identifique se ele é:
#- Uma criança
#- Um adolescente
#- Um adulto
#- Um idoso
idade = int(input('Digite a sua idade: '))

if idade >= 1 and idade <= 12:
    print('Você é uma criança')
elif idade >= 13 and idade <= 17:
    print('Você é um adolescente')
elif idade >= 18 and idade <= 59:
    print('Você é um adulto')
elif idade >= 60:
    print('Você é um idoso')
else:
    print('Entrada inválida.')

#------Maior entre três números------
#Crie um programa em Python que solicite três números ao usuário. Utilize estruturas condicionais para determinar o maior entre eles e apresente o resultado.
a = int(input('Informe o primeiro valor: '))
b = int(input('Informe o segundo valor: '))
c = int(input('Informe o terceiro valor: '))

if a > b and a > c:
    print(a, 'é o maior valor!')
elif b > a and b > c:
    print(b, 'é o maior valor!')
elif c > a and c > b:
    print(c, 'é o maior valor!')
elif a == b and b == c:
    print(f'{a}, {b}, {c} são valores iguais.')
else:
    print('Há dois valores iguais.')

#------Contagem de pares e ímpares------
#Faça um programa que:
#- Leia números inseridos pelo usuário.
#- Calcule e apresente a quantidade de números pares e ímpares inseridos.
#- O processo de leitura deve ser encerrado quando o usuário informar o valor zero.
#- Inclua validações para garantir que apenas números positivos sejam considerados na contagem e nos cálculos.

impar = []
par = []

while True:
    try:
        num = int(input('Digite um valor (0 para encerrar): '))

        if num == 0:
            break

        if num > 0:
            if num % 2 == 0:
                par.append(num)
            else:
                impar.append(num)
        else:
            print("Insira apenas números positivos.")  

    except ValueError:
        print("Entrada inválida! Digite apenas números inteiros.")

print(f'Ímpares: {impar}\nQuantidade: {len(impar)}')
print(f'Pares: {par}\nQuantidade: {len(par)}')

#------Números em ordem crescente------
#Faça um programa que leia três números inteiros e os mostre em ordem crescente.
num = []
quant = 3
for i in range(quant):
    valor = int(input('Digite um valor: '))
    num.append(valor)
num.sort()
print(num)

#------Cálculo de salário líquido------
#Escreva um programa que calcule o salário líquido. O programa deve declarar o salário bruto e o percentual de desconto do Imposto de Renda.
#As alíquotas são:
#- Renda até R$1.903,98: isento de imposto de renda.
#- Renda entre R$1.903,99 e R$2.826,65: alíquota de 7,5%.
#- Renda entre R$2.826,66 e R$3.751,05: alíquota de 15%.
#- Renda entre R$3.751,06 e R$4.664,68: alíquota de 22,5%.
#- Renda acima de R$4.664,69: alíquota máxima de 27,5%.
sal = float(input('Informe seu salário: '))

if sal <= 1903.98:
    print(f'Salário Bruto: {sal}\nDesconto: Isento')
elif sal > 1903.98 and sal <= 2826.65:
    print(f'Salário Bruto: {sal}\nDesconto: {sal*0.075}')
elif sal > 2826.65 and sal <= 3751.05:
    print(f'Salário Bruto: {sal}\nDesconto: {sal*0.15}')
elif sal > 3751.05 and sal <= 4664.68:
    print(f'Salário Bruto: {sal}\nDesconto: {sal*0.225}')
else:
    print(f'Salário Bruto: {sal}\nDesconto: {sal*0.275}')
