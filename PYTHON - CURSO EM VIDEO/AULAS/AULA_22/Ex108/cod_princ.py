import Ex108.moeda as moeda

preco = float(input('Digite o preco: R$'))

print(f'A metade de {moeda.moeda(preco)} = {moeda.moeda(moeda.metade(preco))}')
print(f'O dobro de {moeda.moeda(preco)} = {moeda.moeda(moeda.dobro(preco))}')
print(f'Aumentado em 10%, temos {moeda.moeda(moeda.aumentar(preco))}')
print(f'Reduzido em 13%, temos {moeda.moeda(moeda.diminuir(preco))}')
