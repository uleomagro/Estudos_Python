print('-='*25)

lista = []
lista_par = []
lista_impar = []

while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    if n % 2 == 0:
        lista_par.append(n)
    else:
        lista_impar.append(n)


    # Continuar? 
    while True:
        continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()
        if continuar not in ('S', 'N'):
            print('Entrada invalida, digite apenas S ou N...')
        else:
            break
    if continuar == 'N':
        break

print('==== LISTAS GERADAS ====')
print(f'Lista completa: {lista}')
print(f'Lista somente com numeros pares: {lista_par}')
print(f'Lista somente com numeros impares: {lista_impar}')
print('-=-'*25)