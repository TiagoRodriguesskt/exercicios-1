'''
Docstring for Ex13
Considere a tupla1 e responda as seguintes questões:

tupla1=('A','B','A','Z','Z','X','A','E','K','G','H')

a) mostre na tela o tamanho desta tupla;
b) ordene a tupla e mostre o resultado na tela;
c) mostre na tela o número de ocorrências da string 'A';
d) mostre na tela o número de ocorrências da string 'B';
e) mostre na tela o índice da string 'X';
f) mostre na tela o último elemento da tupla1.
'''

def ex13():
    tupla1 = ('A', 'B', 'A', 'Z', 'Z', 'X', 'A', 'E', 'K', 'G', 'H')
    # a) Tamanho da tupla
    tamanho = len(tupla1)
    print(f"Tamanho da tupla: {tamanho}")
    # b) Tupla ordenada
    tupla_ordenada = tuple(sorted(tupla1))
    print(f"Tupla ordenada: {tupla_ordenada}")
    # c) Número de ocorrências da string 'A'
    ocorrencias_a = tupla1.count('A')   
    print(f"Ocorrências da string 'A': {ocorrencias_a}")    
    # d) Número de ocorrências da string 'B'
    ocorrencias_b = tupla1.count('B')   
    print(f"Ocorrências da string 'B': {ocorrencias_b}")    
    # e) Índice da string 'X'
    indice_x = tupla1.index('X')   
    print(f"Índice da string 'X': {indice_x}")    
    # f) Uúltimo elemento da tupla1
    ultimo_elemento = tupla1[-1]
    print(f"Último elemento da tupla1: {ultimo_elemento}")

if __name__ == "__main__":
    ex13()

if __name__ == "__main__":
    ex13()
