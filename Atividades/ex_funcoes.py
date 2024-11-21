#------Soma de três argumentos------
#Faça um programa com uma função que necessite de três argumentos e que forneça a soma desses três argumentos.
'''
def soma(a,b,c):
    calculo = a + b + c
    print('A soma dos valores é: ', calculo)

a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))

soma(a,b,c)
'''
#------Reverso do número------
#Crie uma função que retorne o reverso de um número inteiro informado. Exemplo: Entrada - 127 → Saída - 721
'''
def reverso(num):
    num = str(num) #transformando a variável do tipo int em string, pois o slicing só funciona em variáveis do tipo string
    num = num[::-1] 
    print(num)

num = int(input('Digite um valor inteiro: '))

reverso(num)
'''
#------Conversão de temperatura------
#Escreva um script que pergunte ao usuário se ele deseja converter uma temperatura de graus Celsius para Fahrenheit ou vice-versa. Para cada opção, crie uma função.
#Plus: Crie uma terceira função que funcione como um menu para o usuário escolher a opção desejada. O menu deve chamar a função de conversão correta.
'''
def celsius(temp):
    calculo = (temp * 1.8) + 32
    print(f'Temperatura em Celsius: {calculo:.2f}')

def fahrenheit(temp):
    calculo = (temp - 32) / 1.8
    print(f'Temperatura em Fahrenheit: {calculo:.2f}')

def menu():
    while True:
        try:
            op = int(input('Escolhe para qual modo deseja converter:\n1 - Para Celsius\n2 - Para Fahrenheit\n'))
                    
            if op == 1:
                temp = float(input('Informe a temperatura: '))
                celsius(temp)
                break
            elif op == 2:
                temp = float(input('Informe a temperatura: '))
                fahrenheit(temp)
                break
            else: 
                print('Opção não identificada. Por favor, tente novamente.')
        except ValueError:
            print('Entrada inválida. Por favor, insira um número.')

menu()
'''
#------Conversão de moedas------
#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e calcule quanto poderia comprar de cada moeda estrangeira. Considere a tabela de conversão abaixo:
#- Dólar Americano: R$ 4,91
#- Peso Argentino: R$ 0,02
#- Dólar Australiano: R$ 3,18
#- Dólar Canadense: R$ 3,64
#- Franco Suíço: R$ 0,42
#- Euro: R$ 5,36
#- Libra Esterlina: R$ 6,21
'''
def moedas(saldo):
    taxas = {}
    taxas = {
        'Dólar Americano': 4.91,
        'Peso': 0.02,
        'Dólar Australiano': 3.18,
        'Dólar Canadense': 3.64,
        'Franco': 0.42,
        'Euro': 5.36,
        'Libra': 6.21
    } 

    print('\n----Conversões----')

    for moeda,taxa in taxas.items():
        calculo = saldo / taxa
        print(f'{moeda}: {calculo:.2f}')
    
saldo = float(input('Informe seu saldo na carteira: '))

moedas(saldo)
'''
#------Contador de vogais------
#Crie uma função chamada contar_vogais que recebe uma string como parâmetro. Implemente a lógica para contar o número de vogais na string e retorne o total de vogais. Solicite ao usuário que insira uma frase e utilize a função para contar as vogais.
'''
def contar_vogais(string):
    qtd = 0
    vogais = 'aeiou'

    for i in string.lower():
        if i in vogais:
            qtd += 1
    
    print(f'Há {qtd} vogais em "{string}"')

string = str(input('Digite algo: '))
contar_vogais(string)
'''
#------Jogo da forca------
#Vamos construir um jogo da forca!
#- O programa escolherá aleatoriamente uma palavra secreta de uma lista predefinida.
#- A palavra secreta será representada por espaços em branco (um para cada letra da palavra).
#- O jogador terá um número limitado de 6 tentativas.
#- A cada tentativa, o jogador pode fornecer uma letra.
#- Se a letra estiver presente na palavra secreta, ela será revelada nas posições correspondentes.
#- Se a letra não estiver na palavra, uma mensagem de erro deverá ser exibida.
#- Após exceder o número máximo de erros, o jogador perde.
#- O jogo continua até que o jogador adivinhe a palavra ou exceda o número máximo de tentativas.
#Dica: Você precisará importar uma biblioteca para resolver esse exercício.
import random

def palavra_aleatoria():
    palavras = ["python", "dados", "listas", "teste"]
    return random.choice(palavras)

def jogar():
    palavra = palavra_aleatoria()
    letras_corretas = []
    letras_erradas = []
    chances = 6

    print('===============================================')
    print('=================JOGO DA FORCA=================')
    print('===============================================')

    print(f'Você tem {chances} chances para acertar a palavra secreta:')

    while True:
        palavra_secreta = ""
        for letra in palavra:
            if letra in letras_corretas:
                palavra_secreta += letra
            else:
                palavra_secreta += "_"

        print(palavra_secreta)
        print("")

        if palavra_secreta == palavra:
            print(f"Parabéns! Você acertou a palavra secreta")
            break

        tentativa = input("Digite uma letra: ").lower()

        if tentativa in palavra:
            letras_corretas.append(tentativa)
            chances -= 1 
            print(f"Você tem {chances} tentativas restantes.")
        else:
            print("Letra errada. :(")
            letras_erradas.append(tentativa)
            chances -= 1 
            print(f"Você tem {chances} tentativas restantes.")

        if chances == 0:
            print("\nSuas chances se esgotaram. Você Perdeu!\nA palavra secreta era: ", palavra)
            break

jogar()