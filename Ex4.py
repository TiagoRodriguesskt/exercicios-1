'''
Docstring for Ex4
Escreva um programa que peça um número inteiro do usuário e mostre se esse número é par ou ímpar. 
A mensagem na tela deverá seguir o seguinte formato:

"O número [número] é [par/ímpar]"

'''

def ex4():
    # Solicita um número inteiro do usuário
    numero = int(input("Digite um número inteiro: "))
    # Verifica se o número é par ou ímpar
    if numero % 2 == 0:
        resultado = "par"
    else:
        resultado = "impar"
    # Exibe o resultado
    print(f"O número {numero} é {resultado}!")
