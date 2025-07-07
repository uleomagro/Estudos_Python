import random
print('=-'*40)

# Sorteia os 5 numeros
numeros = []
def sorteio():
    print('Sorteando 5 valores da lista:', end=' ')
    for c in range(1, 6):
        num = random.randint(0, 50)
        numeros.append(num)
    print(*numeros, 'PRONTO!')
sorteio()

# Soma todos os valores pares
pares = []
def somaPar():
    print(f'Somando os valores pares da lista {numeros}', end='  ')
    for c in numeros:
        if c % 2 == 0:
            pares.append(c)
    if sum(pares) == 0:
        print('  NENHUM NUMERO PAR FOI SORTEADO')
    else:
        print(f'Resultado = {sum(pares)}')
somaPar()

print('=-'*40)