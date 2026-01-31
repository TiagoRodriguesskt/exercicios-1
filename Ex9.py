'''
Docstring for Ex9

Escreva um script para classificar um triângulo de acordo com o tamanho dos seus lados. Considere as seguintes informações:

--> Triângulo equilátero: todos os lados possuem o mesmo tamanho;
--> Trângulo escaleno: todos os lados possuem medidas diferentes;
--> Triângulo isósceles: caracterizado por ter dois lados com o mesmo tamanho.

'''
def classificar_triangulo(lado1, lado2, lado3):
    if lado1 == lado2 == lado3:
        return "Triangulo equilatero!"
    elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
        return "Triangulo escaleno!"
    else:
        return "Triangulo isosceles!"

def ex9():
    lado1 = float(input("Digite o tamanho do lado 1: "))
    lado2 = float(input("Digite o tamanho do lado 2: "))
    lado3 = float(input("Digite o tamanho do lado 3: "))
    classificacao = classificar_triangulo(lado1, lado2, lado3)
    print(f"O triângulo classificado é: {classificacao}")
