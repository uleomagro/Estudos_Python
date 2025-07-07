print('='*80)

lista_produtos = []
nomes = ''
preco = 0
total_gasto = 0
mais_de_1000 = 0
menor_preco = 0 
nome_mais_barato = ''

while True:

    nomes = input('Nome do produto: ')
    preco = float(input('Valor: R$'))
    lista_produtos.append({'nome': nomes, 'preco': preco})

    total_gasto = preco + total_gasto
    if preco > 1000:
        mais_de_1000 += 1
    
    if menor_preco == 0 or preco < menor_preco:
        menor_preco = preco
        nome_mais_barato = nomes

    cont = input('Deseja adicionar mais produtos? [S ou N]: ').upper()
    while cont not in ('S', 'N'):
        cont = input('Digite apenas [S ou N]: ').upper()
    if cont == 'N':
        break

print('=' * 80)
print('Lista de produtos cadastrados:')
for produto in lista_produtos:
    print(f"- {produto['nome']} → R${produto['preco']:.2f}")


print(f'O total gasto na compra foi R${total_gasto:.2f}')
print(f'Temos {mais_de_1000} produto(s) custando mais de R$1000.00')
print(f'O produto mais barato foi {nome_mais_barato} que custa R${menor_preco:.2f}')
print('=' * 80)