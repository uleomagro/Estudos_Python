def fatorial(n, show=False):
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

numero = int(input('Digite um valor: '))

while True:
    mostrar = input('Quer mostrar todo o calculo? [S/N]: ').upper().strip()
    if mostrar not in 'SN':
        print('ERRO!')
    elif mostrar == 'S':
        print(fatorial(numero, show=True))
        break
    elif mostrar == 'N':
        print(fatorial(numero))
        break