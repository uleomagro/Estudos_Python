print('='*80)

print('INSIRA 5 VALORES')

lista = []

for c in range(5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado no posição {pos} da lista...')
                break
            pos += 1
print('-=-'*10)
print(f'Os valores digitados na ordem foram: {lista}')
