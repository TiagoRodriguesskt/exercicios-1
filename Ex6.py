'''
Docstring for Ex6
Escreva um programa que receba dois números de ponto flutuante e mostre na tela o maior número digitado. 
Considere a possibilidade de o usuário digitar dois números iguais.

'''

def ex6():
    # Recebendo dois números de ponto flutuante do usuário
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    # Comparando os números e exibindo o maior ou informando se são iguais
    if num1 > num2:
        print("O maior número é:", num1)
    elif num2 > num1:
        print("O maior número é:", num2)
    else:
        print("Os dois números são iguais:", num1)
    