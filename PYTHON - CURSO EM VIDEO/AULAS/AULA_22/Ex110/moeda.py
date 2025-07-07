def aumentar(v, cond, formato=True):
    soluc = v + (v * cond / 100) 
    return soluc if formato is False else moeda(soluc)

def diminuir(v, cond, formato=True):
    soluc = v - (v * cond / 100)
    return soluc if formato == False else moeda(soluc)

def dobro(v, formato=True):
    dobro = v * 2
    return dobro if not formato else moeda(dobro)

def metade(v, formato=True):
    metad = v / 2
    return metad if not formato else moeda(metad)

def moeda(v=0, moeda='R$'):
    formatado = f'{moeda}{v:.2f}'.replace('.', ',')
    return formatado

def resumo(v=0, cond1=10, cond2=5):
    print('-'*40)
    print('REMUSO DO VALOR'.center(40))
    print('-'*40)
    print(f'{"Preco analisado:":<20}{moeda(v):>20}')
    print(f'{"Dobro do valor:":<20}{dobro(v):>20}')
    print(f'{"Metade do preco:":<20}{metade(v):>20}')
    print(f'{f"{cond1}% de aumento:":<20}{aumentar(v, cond1):>20}')
    print(f'{f"{cond2}% de reducao:":<20}{diminuir(v, cond2):>20}')
    print('='*40)

