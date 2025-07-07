import Ex109.moeda as moeda

preco = float(input('Digite o preco: R$'))

print(f'A metade de {moeda.moeda(preco)} = {moeda.metade(preco, True)}')
print(f'O dobro de {moeda.moeda(preco)} = {moeda.dobro(preco, True)}')
print(f'Aumentado em 10%, temos {moeda.aumentar(preco, True)}')
print(f'Reduzido em 13%, temos {moeda.diminuir(preco, True)}')