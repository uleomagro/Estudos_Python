print('='*80)

numeros = []


while True:
    n = int(input('Adicionar um novo valor à lista: '))   
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado.')

    else:
        print('Numero duplicado. NÃO FOI ADICIONADO')

    while True:
        cont = input('Deseja continuar [S/N]: ').upper().strip()
        if cont in ('S', 'N'):
            break
        print('Resposta inválida. Digite apenas S ou N.')

    if cont == 'N':
        break
numeros.sort()
print('Lista final:', numeros)





print('='*80)