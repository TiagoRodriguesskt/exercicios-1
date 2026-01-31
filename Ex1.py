'''
Docstring for Ex1
DocEscreva um programa que solicite o nome e o sobrenome do usuário. 
Ao final o programa deverá apresentar o nome completo do usuário na tela.string for Ex1

'''

def ex1():
    # Solicita o nome do usuário
    nome = input("Digite seu nome: ")
    # Solicita o sobrenome do usuário
    sobrenome = input("Digite seu sobrenome: ")
    # Combina o nome e o sobrenome para formar o nome completo
    nome_completo = nome + " " + sobrenome
    # Imprime o nome completo do usuário
    print("Seu nome completo é:", nome_completo)
