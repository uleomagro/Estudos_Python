
# Função
def ficha(nome, gols):
    print('=-'*10)
    if nome == '' and gols == 0:
        return f'O jogador <DESCONHECIDO> fez 0 gol(s) no campeonato.'
    elif nome == '':
        return f'O jogador <DESCONHECIDO> fez {gols} gol(s) no campeonato.'
    elif gols == 0:
        return f'O jogador {nome} fez 0 gol(s) no campeonato.'
    else:
        return f'O jogador {nome} fez {gols} gol(s) no campeonato.'


# Programa Principal
print('=-'*10)
nome = input('Nome do Jogador: ').capitalize()
while True:
    gols = input('Número de gols: ')
    if gols == '':
        gols = 0
        print(ficha(nome, gols))
        break
    elif gols.isnumeric():
        print(ficha(nome, gols))
        break
    else:
        print('ERROR!')

print('=-'*10)