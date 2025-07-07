def quadrado():
    tamanho = 10
    print('=' * tamanho)
    for c in range(tamanho - 2):
        print('|' + ' ' * (tamanho - 2) + '|')
    print('=' * tamanho)

def quad_texto():
    texto = str(input('Digita ai: '))
    tamanho_quadrado = len(texto) + 4

    linhas_internas = tamanho_quadrado - 2
    linha_texto = linhas_internas // 2

    print('-' * tamanho_quadrado)
    for i in range(tamanho_quadrado - 2):
        if i == linha_texto:
            conteudo = texto.center(tamanho_quadrado - 2)
            print('|'+conteudo+'|')
        else:
            print('|' + ' ' * (tamanho_quadrado - 2) + '|')
    print('-' * tamanho_quadrado)

def lin(tam):
    print('-' * tam)
#largura = 30
#lin(largura)
#print('OLA MUNDO'.center(largura))
#lin(largura)

def soma(*valores):
    s = sum(valores)
    print(f'Soma: {s}')

def mostrar(*num):
    print('Valores:', num)
    
    # Verifica se todos os itens são números
    if all(isinstance(i, (int, float)) for i in num):
        soma(*num)
    else:
        print('Não posso somar: nem todos os valores são números.')

# Testes
mostrar(1, 2)           # Vai somar
mostrar(1, 2, 3)        # Vai avisar que há mais de 2
mostrar('oi', 2)        # Vai avisar que nem todos são números
mostrar(5.5, 4.5)         # Soma todos com float


def dobrar(*valores):
    for v in valores:
        dobro = v * 2
        print(dobro)

valores_list = []
while True:
    valores = int(input('Digite um valor: '))
    valores_list.append(valores)

    cont = str(input('Quer continuar [S/N]: '))
    if cont in 'Nn':
        break


dobrar(*valores_list)