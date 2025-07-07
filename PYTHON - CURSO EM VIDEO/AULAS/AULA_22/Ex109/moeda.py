def aumentar(v, formato=False):
    aum = 0.10
    soluc = v + (v * aum)
    return soluc if formato is False else moeda(soluc)

def diminuir(v, formato=False):
    dim = 0.13
    soluc = v - (v * dim)
    return soluc if formato == False else moeda(soluc)

def dobro(v, formato=False):
    dobro = v * 2
    return dobro if not formato else moeda(dobro)

def metade(v, formato=False):
    metad = v / 2
    return metad if not formato else moeda(metad)

def moeda(v=0, moeda='R$'):
    formatado = f'{moeda}{v:.2f}'.replace('.', ',')
    return formatado
