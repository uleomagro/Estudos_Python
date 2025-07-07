print('='*80)
print('INICIO'.center(80))
print('='*80)

palavras = ('Cadeia', 'Lula', 'Preso', 'Ladrao', 'Corrupto', 'Arrombado')

for palavra in palavras:
    print(f'Na palavra {palavra} temos: ', end=' ')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
    print()

print('='*80)
print('FIM'.center(80))
print('='*80)