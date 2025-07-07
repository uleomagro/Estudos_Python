#help(print)
#print(input.__doc__)

#def contador(i, f, p):
    # """
    # --> Realiza uma contagem de i até f, com passo p, imprimindo os números.

    # Args:
    #     i (int): Início da contagem.
    #     f (int): Final da contagem.
    #     p (int): Passo da contagem (incremento).

    # Returns:
    #     None
    # """
    # c = i
    # while c <= f:
    #     print(f'{c}', end='..')
    #     c += p
    # print('FIM')

#help(contador)

# Parametros opcionais

#def somar(a=0, b=0, c=0):
    # s = a+b+c
    # print(f'Soma dos valores = {s}')

#somar(1)

# Escopo de variaveis
# Retorno de valores

def somar(a=0, b=0, c=0):
    s = a+ b+ c
    return s

r1 = somar(3, 2, 5)
r2 = somar(1, 7)
r3 = somar(4)
print(f'Meus calculos deram {r1} -> {r2} -> {r3}')