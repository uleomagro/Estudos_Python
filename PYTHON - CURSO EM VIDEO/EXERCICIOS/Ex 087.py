print('=-'*40)

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input('Digite um valor: '))
print('=-'*10)
print(matriz[0])
print(matriz[1])
print(matriz[2])        
print('=-'*10)

# A
pares = 0
for linha in matriz:
    for valor in linha:
        if valor % 2 == 0:
            pares += valor
print(f'Soma dos valores pares = {pares}')

# B
coluna3 = 0
for linha in matriz:
    coluna3 += linha[2]
print(f'Soma dos valores da terceira coluna = {coluna3}')

# C
maior = max(matriz[1])
print(maior)