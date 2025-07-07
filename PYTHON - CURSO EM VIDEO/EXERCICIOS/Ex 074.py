print('='*80)

import random

aleatorios = tuple(random.choices(range(0, 999), k=5))

print(aleatorios)

print(f'Os numeros gerados foram: {aleatorios}')
print(f'O menor numero: {min(aleatorios)}')
print(f'O maior numero: {max(aleatorios)}')

print('FIM')