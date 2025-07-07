print('-='*30)

jogador = {}
gols = []
jogador['Nome'] = str(input('Nome do Jogador: '))

tot_jogos = int(input(f'Quantas partidas o {jogador["Nome"]} teve: '))

for i in range(tot_jogos):
    gol = int(input(f'Quantos gols na {i+1}° partida: '))
    gols.append(gol)

jogador['Gols'] = gols
jogador['Total'] = sum(gols)

print('')
print(jogador)
print('')

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('')

print(f'O jogador {jogador["Nome"]} jogou {tot_jogos} partidas')

for i in range(tot_jogos):
    print(f' => Na partida {i+1}, ele fez {jogador["Gols"][i]}')
print(f'O total de gols foi: {jogador["Total"]}')
print('-='*30)