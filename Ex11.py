'''
Docstring for Ex11
Considere a lista a seguir, que apresenta dados referentes a série temporal de 1900 a 2026. 
Faça o que se pede:

a) Crie uma lista que armazene os 20 primeiros anos da série;
b) Crie uma lista que armazene os anos de 1937 a 1969;
c) Crie uma lista que armazene os anos de 2010 a 2020;
d) Crie uma lista que armazene o último ano da série;
e) Apresente a série temporal de 10 em 10 anos.
f) Apresente a série temporal de 5 em 5 anos.
g) Apresente a série temporal de 1 em 1 ano.
h) Apresente a série temporal de trás para frente.
Anos = [ano for ano in range(1900, 2027)]
lista = 1900 até 2026]

'''

def ex11():
    Anos = list(range(1900, 2026))
    print(Anos)
    print(" ")

    # a) Crie uma lista que armazene os 20 primeiros anos da série;
    print("Os 20 primeiros anos da série são:")
    primeiros_20_anos = Anos[:20]
    print(primeiros_20_anos)
    print("")

    # b) Crie uma lista que armazene os anos de 1937 a 1969;
    print("Lista dos anos de 1937 a 1969:")
    anos_1937_1969 = [ano for ano in range(1937, 1970)]
    print(anos_1937_1969)
    print(" ")

    # c) Crie uma lista que armazene os anos de 2010 a 2020;
    print("Lista dos anos de 2010 a 2020:")
    anos_2010_2020 = [ano for ano in range(2010, 2021)]
    print(anos_2010_2020)
    print(" ")

    # d) Crie uma lista que armazene o último ano da série;
    print("O último ano da série é:")
    ultimo_ano = [Anos[-1]]
    print(ultimo_ano)
    print(" ")

    # e) Apresente a série temporal de 10 em 10 anos.
    print("Série temporal de 10 em 10 anos:")
    serie_10_em_10 = Anos[::10]
    print(serie_10_em_10)
    print(" ")

    # f) Apresente a série temporal de 5 em 5 anos.
    print("Série temporal de 5 em 5 anos:")
    serie_5_em_5 = Anos[::5]
    print(serie_5_em_5)
    print(" ")

    # g) Apresente a série temporal de 1 em 1 ano.
    print("Série temporal de 1 em 1 ano:")
    serie_1_em_1 = Anos[::1]
    print(serie_1_em_1)
    print(" ")

    # h) Apresente a série temporal de trás para frente.
    print("Série temporal de trás para frente:")
    serie_tras_para_frente = Anos[::-1]
    print(serie_tras_para_frente)

if __name__ == "__main__":
    ex11()
