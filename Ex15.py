'''
Docstring for Ex15
Verifique se uma lista é vazia ou não. Caso a lista seja vazia, mostre True na tela, caso contrário False.
'''

def is_list_empty(lst):
    return len(lst) == 0

def ex15():
    # Exemplo de uso
    lista1 = []
    print(is_list_empty(lista1))  # Saída: True

    lista2 = [1, 2, 3]
    print(is_list_empty(lista2))  # Saída: False

if __name__ == "__main__":
    ex15() 
