'''
Docstring for Ex8
Escreva um script que mostre na tela o preço de um produto associado a uma categoria especificada pelo usuário. 
Utilize como referência as informações a seguir. 
Caso o usuário não digite uma categoria válida (número entre 1 e 10) mostre na tela uma mensagem personalizada.

Exemplo: preço x categoria
* Categoria 1 - $ 0,5 
* Categoria 2 - $ 11,3
* Categoria 3 - $ 17,5
* Categoria 4 - $ 33,97
* Categoria 5 - $ 103,47
* Categoria 6 - $ 44,67
* Categoria 7 - $ 12,55
* Categoria 8 - $ 14,87
* Categoria 9 - $ 98,12
* Categoria 10 - $ 131,49

'''
def ex8():
    categoria_precos = {
        1: 0.5,
        2: 11.3,
        3: 17.5,
        4: 33.97,
        5: 103.47,
        6: 44.67,
        7: 12.55,
        8: 14.87,
        9: 98.12,
        10: 131.49
    }
    try:
        categoria = int(input("Digite a categoria do produto (1-10): "))
        preco = categoria_precos[categoria]
        print(f"Preço do produto na categoria {categoria}: ${preco:.2f}")
    except KeyError:
        print("Categoria inválida. Por favor, digite um número entre 1 e 10.")
