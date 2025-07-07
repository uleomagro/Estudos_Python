# Função
def notas(*n, sit=False):
    ficha = {}
    ficha['Total'] = len(n)
    ficha['Maior'] = max(n)
    ficha['Menor'] = min(n)
    ficha['Media'] = sum(n)/len(n)
    if sit == True:
        ficha['Situação'] = ''  
        if ficha['Media'] >= 7:
            ficha['Situação'] = 'BOA'
        elif ficha['Media'] >= 5:
            ficha['Situação'] = 'RAZOAVEL'
        else:
            ficha['Situação'] = 'RUIM'
    return ficha

# Programa principal
resp = notas(5, 3, 5, sit=True)
print(resp)