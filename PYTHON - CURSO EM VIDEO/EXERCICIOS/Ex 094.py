print('=-'*40)
galera = []
pessoa = {}
while True:
    pessoa.clear()
    pessoa['Nome'] = str(input('Nome: ')).strip().capitalize()
    while True:
        pessoa['Sexo'] = str(input('Sexo [M/F]: ')).upper().strip()
        if pessoa['Sexo'] in 'MF':
            break
        print('ERRO! Digite somente [M/F]')
    pessoa['Idade'] = int(input('Idade: '))
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).upper().strip()
        if resp in 'SN':
            break
        print('ERRO! Digite somente [S/N]')
    if resp == 'N':
        break
print('-='*30)
print(galera)
print('-='*30)
# A
print(f'A)  No total, foram cadastradas {len(galera)} pessoas.')
print()
# B
soma = 0
for i in galera:
    soma += i['Idade']
media = soma / len(galera)
print(f'B)  A média de idade é {media:.2f}')
print()
# C
mulheres = []
for i in galera:
    if i['Sexo'] in 'F':
        mulheres.append(i['Nome'])
print(f'C)  As mulheres cadastradas são: {", ".join(mulheres)}')
print()
# D
acima_media_nome = []
for i in galera:
    if i['Idade'] > media:
        acima_media_nome.append(i['Nome'])
print(f'D)  As pessoas com idade acima da média ({media:.2f}) são: {", ".join(acima_media_nome)}')
print('-='*30)
