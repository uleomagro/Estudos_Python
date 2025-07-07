print('=' * 40)
print('             BANCO PYTHON')
print('=' * 40)

valor = int(input('Digite o valor a ser retirado: R$'))

c_50 = valor // 50
resto = valor % 50

c_20 = resto // 20
resto = resto % 20

c_10 = resto // 10
resto = resto % 10

c_1 = resto

print('Você vai receber:')

if c_50 > 0:
    print(f'{c_50} cédula(s) de R$50')

if c_20 > 0:
    print(f'{c_20} cédula(s) de R$20')

if c_10 > 0:
    print(f'{c_10} cédula(s) de R$10')

if c_1 > 0:
    print(f'{c_1} cédula(s) de R$1')

print('=' * 40)
print('Volte sempre ao Banco Python! Tenha um bom dia!')
print('=' * 40)