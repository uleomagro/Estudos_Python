print('=-'*40)

lista = [[], []]
valor = 0 

for c in range(7):
    valor = int(input(f'Digite o {c + 1}° valor: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)

lista[0].sort()
print(lista[0])

lista[1].sort()
print(lista[1])

print('=-'*40)