print('=' * 97)

numeros = 0
soma = 0
quant = 0

while True:
    numeros = int(input('Digite um numero (999 para sair): '))
    if numeros == 999:
        break
    soma += numeros
    quant += 1

print(f'Foram digitados {quant} numeros e a soma entre os numeros digitados é = {soma}')