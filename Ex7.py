'''
Docstring for Ex7
Escreva um programa que inverta uma string. Exemplos:
Exemplo:
Hello World!
Output:
!dlroW olleH

'''
def inverter_string(s):
    return s[::-1]

def ex7():
    frase = input("Digite uma palavra ou frase: ")
    frase_invertida = inverter_string(frase)
    print("Palavra ou frase invertida:", frase_invertida)

if __name__ == "__main__":
    ex7()
