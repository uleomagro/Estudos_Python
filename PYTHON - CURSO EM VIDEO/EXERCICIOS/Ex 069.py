print('='*80)

idade = 0
sexo = 0
mais_dezoito = 0
homens = 0
mulher_menos_vinte = 0

while True:
    idade = int(input('Quantos anos essa pessoa tem: '))
    sexo = input('Qual o sexo? [M] ou [F]: ').upper()
    while sexo not in ('M', 'F'):
        sexo = input('Resposta invalida, digite apensa [M] ou [F]: ').upper()
    if idade >= 18:
        mais_dezoito += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade <20:
        mulher_menos_vinte += 1
    
    continuar = input('Deseja cadastrar outra pessoa? [S] ou [N]: ').upper()
    while continuar not in ('S', 'N'):
        continuar = input('Digite apenas S ou N: ').upper()
    if continuar == 'N':
        break    



print(f'{mais_dezoito} pessoa(s) tem mais de 18 anos.')
print(f'{homens} homen(s) cadastrado(s).')
print(f'{mulher_menos_vinte} mulher(s) tem menos de 20 anos.')