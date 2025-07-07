print('-='*30)
jogador = {}
time = []
gols = []
while True:
    jogador.clear()
    gols.clear()
    jogador['Nome'] = str(input('Nome do Jogador: ')).capitalize()
    tot_jogos = int(input(f'Quantas partidas o {jogador["Nome"]} teve: '))
    for i in range(tot_jogos):
        gol = int(input(f'Quantos gols na {i+1}° partida: '))
        gols.append(gol)
    jogador['Gols'] = gols[:]
    jogador['Total'] = sum(gols)
    time.append(jogador.copy())
    while True:
        resp = input('Quer continuar? [S/N]: ').upper().strip()
        if resp in 'SN':
            break
        else:   
            print('ERRO! Digite apenas S ou N...')
    if resp == 'N':
        break
print('-='*10)
print("\nLISTA DO TIME:")
print(f"{'No.':<4} {'Nome':<10} {'Gols':^20} {'Total':>6}")
for i, jogador in enumerate(time):
    print(f'{i:<4} {jogador['Nome']:<10} {str(jogador['Gols']):^20} {jogador['Total']:>6}')
while True:
    opcao = int(input("\nMostrar dados de qual Jogador? (999 para sair): "))
    if opcao == 999:
        break
    elif opcao < 0 or opcao >= len(time):
        print(f'ERRO! Não existe jogador com o código {opcao}!')
    else:
        print(f'\n-- LEANTAMENTO DO JOGADOR {time[opcao]['Nome']}:')
        for i, gol in enumerate(time[opcao]['Gols']):
            print(f'  No jogo {i+1} fez {gol} gols')