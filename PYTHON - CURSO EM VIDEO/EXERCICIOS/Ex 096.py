def area(larg, compr):
    tot_area = larg * compr
    print(f'A area de um terreno {l} x {c} é igual a = {tot_area}m²')

print('CONTROLE DE TERRENO'.center(25))
print('-'*25)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)