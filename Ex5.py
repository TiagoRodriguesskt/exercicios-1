'''
Docstring for Ex5
O Índice de Massa Corporal (IMC) é utilizado para mensurar o peso ideal de uma pessoa. 
Escreva um programa que peça o nome, a idade , o peso e a altura do usuário. 
Ao final calcule e mostre o resultado do seu IMC e classifique este resultado de acordo com a regra a seguir.

IMC<17 - Muito abaixo do peso ideal
17<=IMC<18,5 - Abaixo do peso
18,5<=IMC<25 - Peso normal
25<=IMC<30 - Acima do peso
30<=IMC<35 - Obesidade I
35<=IMC<40 - Obesidade II (severa)
IMC>=40 - Obesidade III (mórbida)

Lembre que: IMC=massa/(altura*altura)

'''
def calcular_imc(peso, altura):
    return peso / (altura * altura)
def classificar_imc(imc):
    if imc < 17:
        return "Muito abaixo do peso ideal"
    elif 17 <= imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Acima do peso"
    elif 30 <= imc < 35:
        return "Obesidade I"
    elif 35 <= imc < 40:
        return "Obesidade II (severa)"
    else:
        return "Obesidade III (mórbida)"
def ex5():
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))  # noqa: F841
    peso = float(input("Digite seu peso em kg: (ex: 70.5): "))
    altura = float(input("Digite sua altura em metros: (ex: 1.75): "))
    
    imc = calcular_imc(peso, altura)
    classificacao = classificar_imc(imc)
    
    print(f"\n{nome}, seu IMC é: {imc:.2f}")
    print(f"Classificação: {classificacao}")
if __name__ == "__main__":
    ex5()
