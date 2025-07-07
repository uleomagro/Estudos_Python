print('='*80)

times = ('Flamengo', 'Cruzeiro', 'Red Bull Bragantino', 'Palmeiras', 'Fluminense',
 'Bahia', 'Mirassol', 'Atlético-MG', 'Botafogo', 'Ceará',
 'Corinthians', 'Grêmio', 'São Paulo', 'Internacional', 'Juventude',
 'Santos', 'Fortaleza', 'Vasco da Gama', 'Vitória', 'Sport Recife')



print('Os 5 primeiros colocados são: ')  
pos = 1
for colocados in range(0, 5):
    print(f'{pos}° - ', end='')
    print(times[colocados])
    pos += 1
print('='*80)

print('Os 4 ultimos colocados são: ')
pos1 = 17
for ultimo_colocados in range(0, 4):
    print(f'{pos1}° - ', end='')
    print(times[16:][ultimo_colocados])
    pos1 += 1
print('='*80)

print('Times em ordem alfabetica: ')
print(' -> '.join(sorted(times)))
print('='*80)
#for cont in sorted(times):
#    print(cont, end=' -> ')
#print('\b\b\b\b    ') # Gambiarra para apagar a seta \b é backspace

print(f'O time da Juventude esta em: {times.index("Juventude") + 1}°')

print('FIM')