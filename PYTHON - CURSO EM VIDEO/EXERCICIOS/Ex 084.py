print('=-'*25)

temp = []
princ = []
maior = menor = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))

    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]

    princ.append(temp[:])
    temp.clear()

    while True:
        continuar = str(input('Deseja continuar? [S/N]: ')).upper().strip()
        if continuar not in ('S', 'N'):
            print('Entrada invalida...')
        else:
            break
    if continuar == 'N':
        break

# A
print(f'O total de pessoas cadastradas foram {len(princ)}')

# B
print(f'O maior peso foi de {maior}Kg', end =' -> ')
for p in princ:
    if p[1] == maior:
        print([p[0]], end=' ')
print()
print(f'O menor peso foi de {menor}Kg', end =' -> ')
for p in princ:
    if p[1] == menor:
        print([p[0]], end=' ')
print()
