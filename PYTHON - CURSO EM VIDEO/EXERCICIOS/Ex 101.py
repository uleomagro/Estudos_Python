# Função
def voto(ano):
    from datetime import datetime
    ano_atual = datetime.now().year
    idade = ano_atual - ano
    if idade < 18:
        return f'Com {idade} anos: NÃO VOTA.'
    elif idade >= 18 and idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATORIO.'
    elif idade >= 65:
        return f'Com {idade} ano: VOTO OPCIONAL.'

# Programa Principal
print('-'*20)
ano = int(input('Ano de nascimento: '))
print(voto(ano))
print('-'*20)
