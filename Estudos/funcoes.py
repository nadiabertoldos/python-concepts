# ------------------Funções------------------ #
#Grupo de instruções relacionadas que executam uma tarefa
'''
def soma():
    calculo = 10 + 2
    print(f'O resultado da soma é {calculo}')

def subtracao():
    sub = 10 - 2
    print(f'O resultado da subtração é {sub}')
    multiplicacao()

def multiplicacao():
    mult = 10 * 2
    print(f'O resultado da multiplicação é {mult}')

soma()
subtracao()
'''
# ------------------Parâmetros------------------ #
'''
def soma(n1, n2):
    calculo = n1 + n2
    print(f'O resultado da soma é {calculo}')

def subtracao(n1, n2):
    sub = n1 - n2
    print(f'O resultado da subtração é {sub}')

def multiplicacao(n1, n2):
    mult = n1 * n2
    print(f'O resultado da multiplicação é {mult}')
    
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

soma(n1, n2)
subtracao(n1, n2)
multiplicacao(n1, n2)
'''
# ------------------Manipulando Arquivos------------------ #
'''
def multiplicacao():
    mult = 10 * 2
    file = "arquivo.txt"

    #Abertura para escrita
    arquivo_escrita = open(file, "w") #w: write
    arquivo_escrita.write(f"O resultado da multiplicação é {mult}")
    arquivo_escrita.close()

    #Abertura somente para leitura
    arquivo_leitura = open(file, "r") #r: read
    leitura = arquivo_leitura.read()
    print(leitura)
    arquivo_leitura.close()

    #Abertura de arquivos binários
    arquivo_binario = open(file, "wb")

multiplicacao()
'''
# ------------------Tratamento de exceções------------------ #
'''
def divisao(a,b):
    try:
        resultado = a/b
        print(resultado)
    except ZeroDivisionError:
        print('Erro: não é possível dividir um valor por 0.')
    except TypeError as e:
        print(f'Erro: tipo de dado informado incorreto. Detalhes: {e}')
    else:   
        print('Sem exceções.')

divisao(10, 2)
divisao(10, 0)
divisao(10, 'texto')
'''
'''
while True:
    try:
        x = int(input("Insira um número: "))
        break
    except ValueError:
        print("Erro: esse não é um número válido. Tente novamente.")
'''
        