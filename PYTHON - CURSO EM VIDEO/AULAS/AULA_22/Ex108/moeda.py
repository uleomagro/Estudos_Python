def aumentar(v):
    aum = 0.10
    soluc = v + (v * aum)
    return soluc

def diminuir(v):
    dim = 0.13
    soluc = v - (v * dim)
    return soluc

def dobro(v):
    dobro = v * 2
    return dobro

def metade(v):
    metad = v / 2
    return metad

def moeda(v = 0, moeda = 'R$'):
    formatado = f'{moeda}{v:.2f}'.replace('.', ',')
    return formatado

