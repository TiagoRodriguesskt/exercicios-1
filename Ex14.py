'''
Docstring for Ex14
Mude a chave 'valor' do dicionário produto1 para 99.98.

produto1={
    'nome':'produto1',
    'tipo':'categoriaA',
    'valor':'50.5',
    'fornecedor':'ABCD',
}
'''

def ex14():
    produto1={
        'nome':'produto1',
        'tipo':'categoriaA',
        'valor':'50.5',
        'fornecedor':'ABCD',
    }
    produto1['valor'] = 99.98 # type: ignore
    print(produto1)

if __name__ == "__main__":
    ex14()
