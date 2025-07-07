print('='*80)

num = []

for seq in range(5):
    numero = int(input(f'Digite o {seq + 1}* valor: '))
    num.append(numero)

# Numeros digitados
print('-=-'*20)
print(f'Os valores digitados foram {num}')

# Maior
print('-=-'*20)
print(f'O Maior valor digitado foi: {max(num)}')

for pos1, valor1 in enumerate(num):
    if valor1 == max(num):
        print(f'Maior valor nas posicao: {pos1}')

# Menor
print('-=-'*20)
print(f'O menor valor digitado foi: {min(num)}')

for pos2, valor2 in enumerate(num):
    if valor2 == min(num):
        print(f'Maior valor nas posicao: {pos2}')

print('='*80)