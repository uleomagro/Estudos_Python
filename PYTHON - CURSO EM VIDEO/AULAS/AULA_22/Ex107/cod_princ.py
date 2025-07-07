import moeda

preco = float(input('Digite o preco: R$'))

print(f'A metade de {preco} = {moeda.metade(preco):.2f}')
print(f'O dobro de {preco} = {moeda.dobro(preco):.2f}')
print(f'Aumentado em 10%, temos {moeda.aumentar(preco):.2f}')
print(f'Reduzido em 13%, temos {moeda.diminuir(preco):.2f}')
