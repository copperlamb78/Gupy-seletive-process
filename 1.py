# 1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores
# (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, 
# ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
# IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido
# no código;

def VerifyNumber(arg, list):
    if arg in list:
        print('ele pertence!')
    else:
        print('Ele não pertence')

fibonacci = [0,1]

for i in range(100):
    n1 = fibonacci[-2]
    n2 = fibonacci[-1]

    sequenceCalc = n1 + n2
    fibonacci.append(sequenceCalc)
    # print(fibonacci)

print('Verificaremos se pertence a sequencia fibonacci!')
arg = int(input('Escolha um número: '))
VerifyNumber(arg, fibonacci)
