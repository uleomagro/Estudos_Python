print('='*80)

produtos = ('Lapis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 
         'Compasso', 9.99, 'Mochila', 120.32, 'Kit Canetas', 22.30, 'Livro', 34.90)

print('-'*40)
print('LISTAGEM DE PRECOS'.center(40))
print('-'*40)

for indice in range(0, len(produtos), 2):
    nome = produtos[indice]
    preco = produtos[indice + 1]
    print(f'{nome:.<20}R${preco:>7.2f}')

print('-'*40)

print('='*80)