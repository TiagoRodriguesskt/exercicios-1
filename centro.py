from Ex1 import ex1 
from Ex2 import ex2
from Ex3 import ex3
from Ex4 import ex4
from Ex5 import ex5
from Ex6 import ex6
from Ex7 import ex7
from Ex8 import ex8
from Ex9 import ex9
from Ex10 import ex10
from Ex11 import ex11
from Ex12 import ex12
from Ex13 import ex13
from Ex14 import ex14
from Ex15 import ex15

EXERCICIOS = {
    1: ex1, 2: ex2, 3: ex3, 4: ex4, 5: ex5,
    6: ex6, 7: ex7, 8: ex8, 9: ex9, 10: ex10,
    11: ex11, 12: ex12, 13: ex13, 14: ex14, 15: ex15
}

def executar_exercicio(numero):
    """Execute a specific exercise by number."""
    if numero in EXERCICIOS:
        EXERCICIOS[numero]()
    else:
        print(f"Exercício {numero} não encontrado.")

def executar_todos():
    """Execute all exercises in sequence."""
    for numero in sorted(EXERCICIOS.keys()):
        print(f"\n--- Executando Exercício {numero} ---")
        executar_exercicio(numero)

def main():
    """Main menu for user interaction."""
    resposta = input("Deseja executar um exercício específico? (s/n): ").lower()
    
    if resposta == 's':
        try:
            numero = int(input("Digite o número do exercício (1-15): "))
            executar_exercicio(numero)
        except ValueError:
            print("Entrada inválida. Digite um número.")
    else:
        executar_todos()

if __name__ == "__main__":
    main()
